## [0.10.2](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.10.1...v0.10.2) (2026-09-02)

## [0.10.2.20260907.1016] - 2026-09-07

### fix(reseller): update 5 endpoints

#### GET /companies
* api operation id `get-companies` removed and replaced with `list-end-user-companies`


#### POST /search/companies
* api operation id `search-companies` removed and replaced with `search-end-user-companies`


#### POST /search/users
* api operation id `search-users` removed and replaced with `search-end-users`


#### POST /user
* api operation id `create-users` removed and replaced with `create-end-user`


#### GET /users
* api operation id `get-users` removed and replaced with `list-end-users`


## [0.10.2.20260907.0937] - 2026-09-07

### fix(wallet): api operation id `get-batch-credit-balances` removed and replaced with `list-batch-credit-balances` (GET /balances)

#### GET /balances
* api operation id `get-batch-credit-balances` removed and replaced with `list-batch-credit-balances`


## [0.10.2.20260907.0846] - 2026-09-07

### feat(otm)!: update 23 endpoints

#### POST /{contract_id}/search/
* **BREAKING**: the schema of the request property `properties/anyOf[subschema #1: FilterFields]/max_off_nadir/anyOf[subschema #2]//items` became `false`: no value passes validation
* **BREAKING**: the schema of the request property `properties/anyOf[subschema #1: FilterFields]/min_off_nadir/anyOf[subschema #2]//items` became `false`: no value passes validation
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #1: Point]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #2: MultiPoint]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #3: LineString]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #4: MultiLineString]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #5: Polygon]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #6: MultiPolygon]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #1: Point]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #2: MultiPoint]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #3: LineString]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #4: MultiLineString]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #5: Polygon]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #6: MultiPolygon]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #1: Point]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #2: MultiPoint]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #3: LineString]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #4: MultiLineString]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #5: Polygon]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #6: MultiPolygon]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #1: Point]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #2: MultiPoint]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #3: LineString]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #4: MultiLineString]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #5: Polygon]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `intersects/anyOf[subschema #1]/oneOf[subschema #7: GeometryCollection]/geometries/items/oneOf[subschema #6: MultiPolygon]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #1: SearchResponseFeatureStandardFeasibilityRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #2: SearchResponseFeatureAssuredFeasibilityRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #3: SearchResponseFeatureStandardFeasibilityResponse]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #4: SearchResponseFeatureAssuredFeasibilityResponse]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #5: SearchResponseFeatureStandardOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #6: SearchResponseFeatureAssuredOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #7: ResellerSearchResponseFeatureStandardOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/oneOf[subschema #8: ResellerSearchResponseFeatureAssuredOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #1: SearchResponseFeatureStandardFeasibilityRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #2: SearchResponseFeatureAssuredFeasibilityRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #3: SearchResponseFeatureStandardFeasibilityResponse]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #4: SearchResponseFeatureAssuredFeasibilityResponse]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #5: SearchResponseFeatureStandardOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #6: SearchResponseFeatureAssuredOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #7: ResellerSearchResponseFeatureStandardOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/oneOf[subschema #8: ResellerSearchResponseFeatureAssuredOrderRequest]/geometry/anyOf[subschema #1: Point]/bbox` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/tasking/feasibilities/
* api operation id `get-tasking-feasibility-requests` removed and replaced with `list-feasibility-requests`
* added `subschema #1, subschema #2` to the `features/items/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/geometry/bbox` response property `anyOf` list for the response status `200`


#### POST /{contract_id}/tasking/feasibilities/
* api operation id `post-tasking-feasibility` removed and replaced with `create-feasibility-request`
* added `subschema #1, subschema #2` to the `geometry/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `202`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `202`


#### POST /{contract_id}/tasking/feasibilities/orders/{order_id}
* api operation id `post-tasking-order-feasibility` removed and replaced with `create-order-feasibility-request`
* added `subschema #1, subschema #2` to the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `202`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `202`


#### GET /{contract_id}/tasking/feasibilities/{id}
* api operation id `get-tasking-feasibility-request` removed and replaced with `get-feasibility-request`
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/tasking/feasibilities/{id}/response
* api operation id `get-tasking-feasibility-response` removed and replaced with `get-feasibility-response`
* added `subschema #1, subschema #2` to the `features/items/anyOf[subschema #1: StandardFeasibilityResponseFeature]/geometry/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/anyOf[subschema #2: AssuredFeasibilityResponseFeature]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/anyOf[subschema #1: StandardFeasibilityResponseFeature]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/anyOf[subschema #2: AssuredFeasibilityResponseFeature]/geometry/bbox` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/tasking/orders/
* api operation id `get-tasking-orders` removed and replaced with `list-orders`
* added `subschema #1, subschema #2` to the `features/items/anyOf[subschema #1: StoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/anyOf[subschema #2: ResellerStoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/anyOf[subschema #1: StoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/anyOf[subschema #2: ResellerStoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`


#### POST /{contract_id}/tasking/orders/
* api operation id `post-tasking-orders` removed and replaced with `create-order`
* added `subschema #1, subschema #2` to the request body `anyOf` list
* removed `subschema #1, subschema #2` from the request body `anyOf` list
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: StoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `201`
* added `subschema #1, subschema #2` to the `anyOf[subschema #2: ResellerStoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `201`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: StoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `201`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #2: ResellerStoredOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `201`


#### GET /{contract_id}/tasking/orders/{order_id}
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: GetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `anyOf[subschema #2: ResellerGetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: GetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #2: ResellerGetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`


#### PATCH /{contract_id}/tasking/orders/{order_id}
* added `subschema #1, subschema #2` to the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: GetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `anyOf[subschema #2: ResellerGetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: GetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #2: ResellerGetOrderResponse]/geometry/bbox` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/tasking/orders/{order_id}/acquisition/details
* api operation id `get-order-task-details` removed and replaced with `get-order-acquisition`
* the schema of the response property `bbox/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation


#### GET /{contract_id}/tasking/orders/{order_id}/tasks
* api operation id `get-tasking-order-tasks` removed and replaced with `list-order-tasks`
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/acquisition/anyOf[subschema #1: TaskAcquisition]/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/acquisition/anyOf[subschema #1: TaskAcquisition]/geometry/bbox` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/tasking/outages/
* api operation id `get-unplanned-outages` removed and replaced with `list-unplanned-outages`


#### POST /{contract_id}/tasking/price/
* api operation id `get-price` removed and replaced with `calculate-price`
* added `subschema #1, subschema #2` to the `geometry/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `200`


#### POST /{contract_id}/tasking/price/{order_id}
* added `subschema #1, subschema #2` to the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `original_order/geometry/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `updated_order/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `original_order/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `updated_order/geometry/bbox` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/tasking/series/
* api operation id `get-tasking-series` removed and replaced with `list-series`
* added `subschema #1, subschema #2` to the `bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `features/items/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/geometry/bbox` response property `anyOf` list for the response status `200`


#### POST /{contract_id}/tasking/series/
* api operation id `post-tasking-series` removed and replaced with `create-series`
* added `subschema #1, subschema #2` to the `geometry/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `bbox` response property `anyOf` list for the response status `201`
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `201`
* removed `subschema #1, subschema #2` from the `bbox` response property `anyOf` list for the response status `201`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `201`


#### POST /{contract_id}/tasking/series/price/
* api operation id `post-tasking-series-price` removed and replaced with `calculate-series-price-estimate`
* added `subschema #1, subschema #2` to the `geometry/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/bbox` request property `anyOf` list


#### GET /{contract_id}/tasking/series/{series_id}
* api operation id `get-tasking-series-by-id` removed and replaced with `get-series`
* added `subschema #1, subschema #2` to the `bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `200`


#### PATCH /{contract_id}/tasking/series/{series_id}
* api operation id `edit-tasking-series` removed and replaced with `edit-series`
* added `subschema #1, subschema #2` to the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `geometry/anyOf[subschema #1: Point]/bbox` request property `anyOf` list
* added `subschema #1, subschema #2` to the `bbox` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `geometry/bbox` response property `anyOf` list for the response status `200`


#### POST /{contract_id}/tasking/series/{series_id}/cancel
* api operation id `cancel-tasking-series` removed and replaced with `cancel-series`


#### GET /{contract_id}/tasking/series/{series_id}/download
* api operation id `download-tasking-series` removed and replaced with `download-series`


#### GET /{contract_id}/tasking/series/{series_id}/orders/
* api operation id `get-tasking-series-orders` removed and replaced with `list-series-orders`
* added `subschema #1, subschema #2` to the `features/items/geometry/bbox` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `features/items/geometry/bbox` response property `anyOf` list for the response status `200`

#### Description Updates
* 18 description(s) modified


## [0.10.2.20260903.0941] - 2026-09-03

### fix(cos): update 5 endpoints

#### GET /{contract_id}/
* the schema of the response property `orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation


#### POST /{contract_id}/
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `201`: no value passes validation
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `201`: no value passes validation
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `201`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `201`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `201`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `201`: no value passes validation


#### POST /{contract_id}/search/
* the schema of the response property `orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation


#### GET /{contract_id}/{order_id}
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation


#### PATCH /{contract_id}/{order_id}
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #1: PointGeometry]/coordinates/items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates/items/items//items` became `false` for the status `200`: no value passes validation
* the schema of the response property `anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/bbox/items` became `false` for the status `200`: no value passes validation


## [0.10.2.20260902.1457] - 2026-09-02

### feat(wallet): update GET /balances, GET /{contract_id}/credit

#### GET /balances
* response property `balances/additionalProperties/balance` deprecated
* added the required property `balances/additionalProperties/credit_available` to the response with the `200` status
* added the required property `balances/additionalProperties/credit_fulfilled` to the response with the `200` status
* added the required property `balances/additionalProperties/credit_reserved` to the response with the `200` status


#### GET /{contract_id}/credit
* response property `balance` deprecated
* added the required property `credit_available` to the response with the `200` status
* added the required property `credit_fulfilled` to the response with the `200` status
* added the required property `credit_reserved` to the response with the `200` status

#### Description Updates
* 4 description(s) modified


## [0.10.2.20260902.1436] - 2026-09-02

### fix(otm): 6 changes to GET /{contract_id}/tasking/orders/{order_id}/tasks

#### GET /{contract_id}/tasking/orders/{order_id}/tasks
* removed the `planned` enum value from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/status` response property for the response status `200`
* removed the `planned` enum value from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/status_history/items/status_from/anyOf[subschema #1: UserFacingTaskStatus]/` response property for the response status `200`
* removed the `planned` enum value from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/status_history/items/status_to` response property for the response status `200`
* removed the `rejected` enum value from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/status` response property for the response status `200`
* removed the `rejected` enum value from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/status_history/items/status_from/anyOf[subschema #1: UserFacingTaskStatus]/` response property for the response status `200`
* removed the `rejected` enum value from the `anyOf[subschema #1: ListOrderTasksResponse]/tasks/items/status_history/items/status_to` response property for the response status `200`

#### Description Updates
* 1 description(s) modified



### Bug Fixes

* **builder:** collapse json schema 2020-12 tuple arrays
* **builder:** emit str-mixin enums for python 3.10 compatibility
* **builder:** skip sdk generation on python 3.10
* **builder:** unwrap 0.29.1 tainted string wrappers before emitting code

## [0.10.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.10.0...v0.10.1) (2026-08-28)


### Bug Fixes

* **core:** serialize dict query params as JSON

# [0.10.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.9.0...v0.10.0) (2026-08-26)


### Bug Fixes

* **builder:** apply by_alias to list request bodies
* **builder:** key hypothesis example cache on spec content
* **builder:** scope example cache pruning to the spec environment
* **ci:** rebase before pushing CHANGELOG in release workflow
* **misc:** stop tracking generated test_schemas.py fixtures


### Features

* **builder:** omit unset fields from request bodies
* **core:** add x-download-request-id header to download endpoints

# [0.9.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.8.0...v0.9.0) (2026-05-07)

## [0.9.0.20260824.1429] - 2026-08-24

### feat(otm): 3 changes to PATCH /{contract_id}/tasking/series/{series_id}

#### PATCH /{contract_id}/tasking/series/{series_id}
* added `#/components/schemas/StructuredErrorResponse, #/components/schemas/ErrorResponse` to the response body `anyOf` list for the response status `409`
* the response's body `type` changed from `object` to `any` for status `409`
* removed the required property `detail` from the response with the `409` status

#### Description Updates
* 2 description(s) modified


## [0.9.0.20260805.1107] - 2026-08-05

### feat(id): update 8 endpoints

####  
* removed the schema `ResellerNotificationCategory`
* removed the schema `ResellerNotificationConfig`
* removed the schema `ResellerNotificationDescription`
* removed the schema `ResellerNotificationUpdate`


#### GET /user/details
* removed `#/components/schemas/ResellerNotificationCategory` from the `user_metadata/notifications/anyOf[subschema #1]/items/category` response property `anyOf` list for the response status `200`


#### PUT /user/settings
* removed `subschema #2` from the `notifications` request property `anyOf` list
* removed `#/components/schemas/ResellerNotificationCategory` from the `user_metadata/notifications/anyOf[subschema #1]/items/category` response property `anyOf` list for the response status `200`


#### GET /webhooks/
* removed `#/components/schemas/NotificationDescription, #/components/schemas/ResellerNotificationDescription` from the `webhooks/items/event_types/items/` response property `anyOf` list for the response status `200`
* the `webhooks/items/event_types/items/` response's property `type` was narrowed from `any` to `object` for status `200`
* added the required property `webhooks/items/event_types/items/description` to the response with the `200` status
* added the required property `webhooks/items/event_types/items/name` to the response with the `200` status
* added the required property `webhooks/items/event_types/items/topic` to the response with the `200` status


#### POST /webhooks/
* removed `#/components/schemas/NotificationDescription, #/components/schemas/ResellerNotificationDescription` from the `event_types/items/` response property `anyOf` list for the response status `200`
* the `event_types/items/` response's property `type` was narrowed from `any` to `object` for status `200`
* added the required property `event_types/items/description` to the response with the `200` status
* added the required property `event_types/items/name` to the response with the `200` status
* added the required property `event_types/items/topic` to the response with the `200` status


#### GET /webhooks/{id}
* removed `#/components/schemas/NotificationDescription, #/components/schemas/ResellerNotificationDescription` from the `event_types/items/` response property `anyOf` list for the response status `200`
* the `event_types/items/` response's property `type` was narrowed from `any` to `object` for status `200`
* added the required property `event_types/items/description` to the response with the `200` status
* added the required property `event_types/items/name` to the response with the `200` status
* added the required property `event_types/items/topic` to the response with the `200` status


#### PATCH /webhooks/{id}
* removed `#/components/schemas/NotificationDescription, #/components/schemas/ResellerNotificationDescription` from the `event_types/items/` response property `anyOf` list for the response status `200`
* the `event_types/items/` response's property `type` was narrowed from `any` to `object` for status `200`
* added the required property `event_types/items/description` to the response with the `200` status
* added the required property `event_types/items/name` to the response with the `200` status
* added the required property `event_types/items/topic` to the response with the `200` status


#### POST /webhooks/{id}/rotate
* removed `#/components/schemas/NotificationDescription, #/components/schemas/ResellerNotificationDescription` from the `event_types/items/` response property `anyOf` list for the response status `200`
* the `event_types/items/` response's property `type` was narrowed from `any` to `object` for status `200`
* added the required property `event_types/items/description` to the response with the `200` status
* added the required property `event_types/items/name` to the response with the `200` status
* added the required property `event_types/items/topic` to the response with the `200` status


#### POST /webhooks/{id}/test
* removed `#/components/schemas/NotificationDescription, #/components/schemas/ResellerNotificationDescription` from the `event_types/items/` response property `anyOf` list for the response status `200`
* the `event_types/items/` response's property `type` was narrowed from `any` to `object` for status `200`
* added the required property `event_types/items/description` to the response with the `200` status
* added the required property `event_types/items/name` to the response with the `200` status
* added the required property `event_types/items/topic` to the response with the `200` status


## [0.9.0.20260724.1338] - 2026-07-24

### feat(otm): endpoint added (GET /{contract_id}/tasking/series/{series_id}/download)

#### GET /{contract_id}/tasking/series/{series_id}/download
* endpoint added


## [0.9.0.20260717.1101] - 2026-07-17

### feat(otm): update 4 endpoints

#### GET /{contract_id}/tasking/series/
* added the optional property `features/items/properties/order_parameters/addon:withhold` to the response with the `200` status
* added the optional property `features/items/properties/order_parameters/licence_level` to the response with the `200` status
* added the optional property `features/items/properties/order_parameters/max_cloud_cover` to the response with the `200` status
* added the optional property `features/items/properties/order_parameters/max_off_nadir` to the response with the `200` status
* added the optional property `features/items/properties/order_parameters/min_off_nadir` to the response with the `200` status
* added the optional property `features/items/properties/order_parameters/product` to the response with the `200` status
* added the optional property `features/items/properties/order_parameters/satvu:day_night_mode` to the response with the `200` status


#### POST /{contract_id}/tasking/series/
* added the optional property `properties/order_parameters/addon:withhold` to the response with the `201` status
* added the optional property `properties/order_parameters/licence_level` to the response with the `201` status
* added the optional property `properties/order_parameters/max_cloud_cover` to the response with the `201` status
* added the optional property `properties/order_parameters/max_off_nadir` to the response with the `201` status
* added the optional property `properties/order_parameters/min_off_nadir` to the response with the `201` status
* added the optional property `properties/order_parameters/product` to the response with the `201` status
* added the optional property `properties/order_parameters/satvu:day_night_mode` to the response with the `201` status


#### GET /{contract_id}/tasking/series/{series_id}
* added the optional property `properties/order_parameters/addon:withhold` to the response with the `200` status
* added the optional property `properties/order_parameters/licence_level` to the response with the `200` status
* added the optional property `properties/order_parameters/max_cloud_cover` to the response with the `200` status
* added the optional property `properties/order_parameters/max_off_nadir` to the response with the `200` status
* added the optional property `properties/order_parameters/min_off_nadir` to the response with the `200` status
* added the optional property `properties/order_parameters/product` to the response with the `200` status
* added the optional property `properties/order_parameters/satvu:day_night_mode` to the response with the `200` status


#### PATCH /{contract_id}/tasking/series/{series_id}
* added the optional property `properties/order_parameters/addon:withhold` to the response with the `200` status
* added the optional property `properties/order_parameters/licence_level` to the response with the `200` status
* added the optional property `properties/order_parameters/max_cloud_cover` to the response with the `200` status
* added the optional property `properties/order_parameters/max_off_nadir` to the response with the `200` status
* added the optional property `properties/order_parameters/min_off_nadir` to the response with the `200` status
* added the optional property `properties/order_parameters/product` to the response with the `200` status
* added the optional property `properties/order_parameters/satvu:day_night_mode` to the response with the `200` status



### Features

* **builder:** add extra_body kwarg for forward-compat body fields
* **builder:** propagate OpenAPI discriminators to generated models

# [0.8.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.7.0...v0.8.0) (2026-04-17)

## [0.8.0.20260429.1023] - 2026-04-29

### feat(cos): update 4 endpoints

####  
* removed the schema `UnprocessableResponse`
* removed the schema `ValidationErrorDetail`


#### POST /{contract_id}/
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: OrderSubmissionPayload]/item_id` request property `anyOf` list
* added `subschema #1, subschema #2` to the `anyOf[subschema #2: ResellerSubmissionOrderPayload]/item_id` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: OrderSubmissionPayload]/item_id` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `anyOf[subschema #2: ResellerSubmissionOrderPayload]/item_id` request property `anyOf` list


#### POST /{contract_id}/price
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: PriceRequest]/item_id` request property `anyOf` list
* added `subschema #1, subschema #2` to the `anyOf[subschema #2: ResellerPriceRequest]/item_id` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: PriceRequest]/item_id` request property `anyOf` list
* removed `subschema #1, subschema #2` from the `anyOf[subschema #2: ResellerPriceRequest]/item_id` request property `anyOf` list
* added `subschema #1, subschema #2` to the `anyOf[subschema #1: OrderPrice]/item_id` response property `anyOf` list for the response status `200`
* added `subschema #1, subschema #2` to the `anyOf[subschema #2: ResellerOrderPrice]/item_id` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #1: OrderPrice]/item_id` response property `anyOf` list for the response status `200`
* removed `subschema #1, subschema #2` from the `anyOf[subschema #2: ResellerOrderPrice]/item_id` response property `anyOf` list for the response status `200`


#### GET /{contract_id}/{order_id}/download
* for the `query` request parameter `primary_formats`, default value `[geotiff]` was added
* `query` request parameter `collections` list-of-types was narrowed by removing types `null`
* `query` request parameter `primary_formats` list-of-types was narrowed by removing types `null`
* for the `query` request parameter `collections`, the type/format was changed from ``/`` to `array`/``
* for the `query` request parameter `primary_formats`, the type/format was changed from ``/`` to `array`/``
* the response property `detail` became optional for the status `422`
* response property `detail` list-of-types was narrowed by removing types `string` from media type `application/json` of response `422`


#### GET /{contract_id}/{order_id}/{item_id}/download
* for the `query` request parameter `primary_formats`, default value `[geotiff]` was added
* `query` request parameter `primary_formats` list-of-types was narrowed by removing types `null`
* for the `query` request parameter `primary_formats`, the type/format was changed from ``/`` to `array`/``
* the response property `detail` became optional for the status `422`
* response property `detail` list-of-types was narrowed by removing types `string` from media type `application/json` of response `422`

#### Description Updates
* 4 description(s) modified


## [0.8.0.20260427.1612] - 2026-04-27

### feat(otm): update GET /{contract_id}/tasking/orders/{order_id}/tasks, POST /{contract_id}/tasking/orders/

#### POST /{contract_id}/tasking/orders/
* added the non-success response with the status `503`


#### GET /{contract_id}/tasking/orders/{order_id}/tasks
* endpoint added



### Features

* **builder:** rename generated `schema` field to `schema_`

# [0.7.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.6.0...v0.7.0) (2026-04-01)

## [0.7.0.20260415.0826] - 2026-04-15

### fix(cos): update GET /{contract_id}/{order_id}/download, GET /{contract_id}/{order_id}/{item_id}/download

#### GET /{contract_id}/{order_id}/download
* response property `detail` list-of-types was widened by adding types `array` to media type `application/json` of response `422`


#### GET /{contract_id}/{order_id}/{item_id}/download
* response property `detail` list-of-types was widened by adding types `array` to media type `application/json` of response `422`


## [0.7.0.20260409.1312] - 2026-04-09

### feat(cos): update API descriptions

#### Description Updates
* 1 description(s) modified


## [0.7.0.20260409.0911] - 2026-04-09

### feat(otm): added the non-success response with the status '400' (POST /{contract_id}/search/)

#### POST /{contract_id}/search/
* added the non-success response with the status '400'


## [0.7.0.20260408.1657] - 2026-04-08

### feat(id): added the non-success response with the status '400' (PATCH /webhooks/{id})

#### PATCH /webhooks/{id}
* added the non-success response with the status '400'



### Bug Fixes

* **builder:** handle nullable and date format patterns in test schema cleaning
* **ci:** invalidate hypothesis cache when schema cleaning changes


### Features

* **builder:** commit auto-generated SDK code to repo

# [0.6.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.5.1...v0.6.0) (2026-03-26)

## [0.6.0.20260401.0948] - 2026-04-01

### fix(reseller): update GET /users, POST /search/users, POST /user

#### POST /search/users
* the 'users/items/user_email' response's property type/format changed from 'string'/'email' to 'string'/'' for status '200'


#### POST /user
* the '/items/user_email' request property type/format changed from 'string'/'email' to 'string'/''
* the '/items/user_email' response's property type/format changed from 'string'/'email' to 'string'/'' for status '201'


#### GET /users
* the 'users/items/user_email' response's property type/format changed from 'string'/'email' to 'string'/'' for status '200'



### Bug Fixes

* **ci:** pass spec caching config as Dagger function params
* **core:** handle Link models without method attribute in pagination


### Features

* **builder:** auto-generate tests for pagination iterator methods

## [0.5.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.5.0...v0.5.1) (2026-03-12)

## [0.5.1.20260324.0957] - 2026-03-24

### feat(cos): update 5 endpoints

#### GET /{contract_id}/
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### POST /{contract_id}/
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'


#### POST /{contract_id}/search/
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### GET /{contract_id}/{order_id}
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### PATCH /{contract_id}/{order_id}
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacLink, #/components/schemas/LegacyLink' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/StacPropertiesAcquisition, #/components/schemas/LegacyProperties' to the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/LinksV10, #/components/schemas/LinksV9' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/links/items/' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/StacPropertiesV10, #/components/schemas/PropertiesV9' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/anyOf[subschema #1: Order]/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #3: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


## [0.5.1.20260318.1607] - 2026-03-18

### feat(reseller): update GET /companies, POST /search/companies

#### GET /companies
* added the required property 'companies/items/country_code' to the response with the '200' status


#### POST /search/companies
* added the required property 'companies/items/country_code' to the response with the '200' status


## [0.5.1.20260317.1156] - 2026-03-17

### feat(cos): update 7 endpoints

#### GET /{contract_id}/
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### POST /{contract_id}/
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '201' status
* removed the optional property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '201' status
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '201'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '201'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '201'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '201'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '201'
* the 'coordinates' response's property default value '[]' was removed for the status '201'
* the 'coordinates' response's property default value '[]' was removed for the status '201'
* the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '201'
* the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '201'
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '201' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '201' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '201' status


#### POST /{contract_id}/price
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status


#### POST /{contract_id}/search/
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### GET /{contract_id}/{order_id}
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### PATCH /{contract_id}/{order_id}
* added the optional property 'detail/items/ctx' to the response with the '422' status
* added the optional property 'detail/items/input' to the response with the '422' status
* removed the optional property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* removed the optional property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/stac_metadata' from the response with the '200' status
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Order, subschema #2' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response property 'anyOf' list for the response status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' became optional for the status '200'
* the response property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the response property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/geometry/anyOf[subschema #2: PolygonGeometry]/coordinates' became required for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the 'coordinates' response's property default value '[]' was removed for the status '200'
* the '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* the '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties' response's property type/format changed from 'object'/'' to ''/'' for status '200'
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #1: FeatureCollection_Order_ -> subschema #1: FeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/created_at' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/item_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/order_id' from the response with the '200' status
* removed the required property '/anyOf[subschema #2: ResellerFeatureCollection_Order_ -> subschema #2: ResellerFeatureCollection[Order]]/features/items/properties/price' from the response with the '200' status


#### GET /{contract_id}/{order_id}/{item_id}/download
* for the 'path' request parameter 'item_id', the maxLength was set to '256'

#### Description Updates
* 167 description(s) modified


## [0.5.1.20260317.1057] - 2026-03-17

### feat(otm): update API descriptions

#### Description Updates
* 4 description(s) modified



### Bug Fixes

* **builder:** resolve relative $ref paths in OpenAPI specs

# [0.5.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.4.0...v0.5.0) (2026-01-20)

## [0.5.0.20260127.1235] - 2026-01-27

### feat(wallet): update API descriptions

#### Description Updates
* 4 description(s) modified


## [0.5.0.20260127.1115] - 2026-01-27

### feat(cos): update 5 endpoints

#### GET /{contract_id}/
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### POST /{contract_id}/
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '201'


#### POST /{contract_id}/search/
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the 'orders/items/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### GET /{contract_id}/{order_id}
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'


#### PATCH /{contract_id}/{order_id}
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* added '#/components/schemas/event_schema_registry__models__imagery__image_published_9__Polygon' to the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #1: StacPropertiesV9]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #1: FeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'
* removed '#/components/schemas/event_schema_registry__models__imagery__image_published_8__Polygon' from the '/anyOf[subschema #2: ResellerFeatureCollection_Order_]/features/items/properties/stac_metadata/anyOf[subschema #1: StacMetadata]/properties/anyOf[subschema #2: StacPropertiesV7]/proj:geometry' response property 'anyOf' list for the response status '200'

#### Description Updates
* 1 description(s) modified



### Features

* **builder:** add hypothesis example caching for faster tests

# [0.4.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.3.1...v0.4.0) (2026-01-15)


### Features

* **builder:** add conditional test generation via SATVU_GENERATE_TESTS
* **build:** exclude tests and builder from wheel distribution

## [0.3.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.3.0...v0.3.1) (2026-01-14)


### Bug Fixes

* **auth:** handle malformed JWTs in expiration check
* **auth:** make MemoryCache instance-level to prevent token leakage
* **misc:** export OpenAPI spec cache from Dagger container
* **release:** set git identity before creating annotated tag

# [0.3.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.2.0...v0.3.0) (2026-01-07)

## [0.3.0.20260113.1752] - 2026-01-13

### feat(reseller): update API descriptions

#### Description Updates
* 1 description(s) modified


## [0.3.0.20260113.1724] - 2026-01-13

### feat(id): update API descriptions

#### Description Updates
* 4 description(s) modified


## [0.3.0.20260112.1536] - 2026-01-12

### feat(policy): update API descriptions

#### Description Updates
* 6 description(s) modified


## [0.3.0.20260112.1243] - 2026-01-12

### feat(otm): update API descriptions

#### Description Updates
* 2 description(s) modified



### Bug Fixes

* handle pook mock responses in stdlib adapter streaming
* **misc:** include scope in changelog entries
* **release:** anchor version grep to start of line


### Features

* add Jinja2 templates for streaming download tests
* integrate streaming test generation into build

# [0.2.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.1...v0.2.0) (2025-12-19)

### Features

- **core:** rename package and module to satvu
- **release:** implement timestamp versioning for API-triggered releases

## [0.1.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.0...v0.1.1) (2025-12-19)

### Bug Fixes

- **core:** add docstring for SatVuSDK.__init__

# [0.1.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.0.0...v0.1.0) (2025-12-19)

### Features

- **core:** add docstring for the SatVuSDK class
