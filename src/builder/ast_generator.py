"""AST-based code generation for streaming download methods.

This module provides robust, type-safe code generation using Python's AST module
instead of fragile string templates. Guarantees syntactically correct Python code.
"""

import ast

from builder.streaming_detector import StreamingEndpointConfig


class ASTMethodBuilder:
    """Builder for generating streaming method AST nodes."""

    def __init__(self, config: StreamingEndpointConfig):
        """
        Initialize builder with streaming endpoint configuration.

        Args:
            config: Configuration for the streaming endpoint
        """
        self.config = config

    def build_method(self) -> ast.FunctionDef:
        """
        Build complete streaming method as AST node.

        Returns:
            AST FunctionDef node for the streaming method
        """
        # Path params are always required (used in URL formatting)
        path_params = self.config.path_params

        # Query params are all optional (added to params dict with defaults)
        query_params = self.config.query_params

        # Build function signature
        args = self._build_arguments(path_params, query_params)

        # Build function body
        body = self._build_body(path_params, query_params)

        # Build docstring
        docstring_node = self._build_docstring(path_params, query_params)

        # Combine docstring + body
        full_body = [docstring_node] + body

        # Build return annotation
        return_annotation = self._build_return_annotation()

        return ast.FunctionDef(
            name=self.config.stream_method,
            args=args,
            body=full_body,
            decorator_list=[],
            returns=return_annotation,
            lineno=0,
        )

    def _build_arguments(
        self,
        path_params: list[tuple[str, str]],
        query_params: list[tuple[str, str]],
    ) -> ast.arguments:
        """Build function arguments with defaults."""
        # Start with self
        args = [ast.arg(arg="self", annotation=None)]

        # Add path params (required positional - contract_id, order_id, etc.)
        for name, type_ in path_params:
            args.append(ast.arg(arg=name, annotation=parse_type_annotation(type_)))

        # Add output_path (required positional)
        args.append(
            ast.arg(
                arg="output_path",
                annotation=ast.BinOp(
                    left=ast.Name(id="Path", ctx=ast.Load()),
                    op=ast.BitOr(),
                    right=ast.Name(id="str", ctx=ast.Load()),
                ),
            )
        )

        # Add query params as keyword-only with None defaults
        positional_args = []
        kw_args = []
        kw_defaults: list[ast.expr | None] = []

        for name, type_ in query_params:
            kw_args.append(
                ast.arg(
                    arg=name,
                    annotation=parse_type_annotation(type_),
                )
            )
            # All query params default to None
            kw_defaults.append(ast.Constant(value=None))

        # Add standard streaming params (chunk_size, progress_callback, timeout)
        # plus the poll/tracking params forwarded to stream_when_ready.
        kw_args.extend(
            [
                ast.arg(
                    arg="chunk_size", annotation=ast.Name(id="int", ctx=ast.Load())
                ),
                ast.arg(
                    arg="progress_callback",
                    annotation=ast.BinOp(
                        left=ast.Subscript(
                            value=ast.Name(id="Callable", ctx=ast.Load()),
                            slice=ast.Tuple(
                                elts=[
                                    ast.List(
                                        elts=[
                                            ast.Name(id="int", ctx=ast.Load()),
                                            ast.BinOp(
                                                left=ast.Name(id="int", ctx=ast.Load()),
                                                op=ast.BitOr(),
                                                right=ast.Constant(value=None),
                                            ),
                                        ],
                                        ctx=ast.Load(),
                                    ),
                                    ast.Constant(value=None),
                                ],
                                ctx=ast.Load(),
                            ),
                            ctx=ast.Load(),
                        ),
                        op=ast.BitOr(),
                        right=ast.Constant(value=None),
                    ),
                ),
                ast.arg(
                    arg="timeout",
                    annotation=ast.BinOp(
                        left=ast.Name(id="int", ctx=ast.Load()),
                        op=ast.BitOr(),
                        right=ast.Constant(value=None),
                    ),
                ),
                ast.arg(
                    arg="max_wait_seconds",
                    annotation=ast.Name(id="float", ctx=ast.Load()),
                ),
                ast.arg(
                    arg="poll_interval",
                    annotation=ast.BinOp(
                        left=ast.Name(id="float", ctx=ast.Load()),
                        op=ast.BitOr(),
                        right=ast.Constant(value=None),
                    ),
                ),
                ast.arg(
                    arg="request_id",
                    annotation=ast.BinOp(
                        left=ast.Name(id="str", ctx=ast.Load()),
                        op=ast.BitOr(),
                        right=ast.Constant(value=None),
                    ),
                ),
                ast.arg(
                    arg="on_event",
                    annotation=ast.BinOp(
                        left=ast.Subscript(
                            value=ast.Name(id="Callable", ctx=ast.Load()),
                            slice=ast.Tuple(
                                elts=[
                                    ast.List(
                                        elts=[
                                            ast.Name(
                                                id="DownloadEvent", ctx=ast.Load()
                                            ),
                                        ],
                                        ctx=ast.Load(),
                                    ),
                                    ast.Constant(value=None),
                                ],
                                ctx=ast.Load(),
                            ),
                            ctx=ast.Load(),
                        ),
                        op=ast.BitOr(),
                        right=ast.Constant(value=None),
                    ),
                ),
            ]
        )
        kw_defaults.extend(
            [
                ast.Constant(value=self.config.default_chunk_size),
                ast.Constant(value=None),  # progress_callback default
                ast.Constant(value=None),  # timeout default
                # max_wait_seconds default references the core constant so the
                # generated code stays in sync with SDKClient.stream_when_ready.
                ast.Name(id="DEFAULT_MAX_WAIT_SECONDS", ctx=ast.Load()),
                ast.Constant(value=None),  # poll_interval default
                ast.Constant(value=None),  # request_id default
                ast.Constant(value=None),  # on_event default
            ]
        )

        return ast.arguments(
            posonlyargs=positional_args,
            args=args,
            kwonlyargs=kw_args,
            kw_defaults=kw_defaults,
            defaults=[],
        )

    def _build_body(
        self,
        path_params: list[tuple[str, str]],
        query_params: list[tuple[str, str]],
    ) -> list[ast.stmt]:
        """Build method body statements."""
        body: list[ast.stmt] = []

        # 1. Build params dict (redirect + all query params)
        params_dict_keys: list[ast.expr | None] = [ast.Constant(value="redirect")]
        params_dict_values: list[ast.expr] = [ast.Constant(value=True)]

        # Add all query params to params dict
        for name, _ in query_params:
            params_dict_keys.append(ast.Constant(value=name))
            params_dict_values.append(ast.Name(id=name, ctx=ast.Load()))

        body.append(
            ast.Assign(
                targets=[ast.Name(id="params", ctx=ast.Store())],
                value=ast.Dict(keys=params_dict_keys, values=params_dict_values),
            )
        )

        # 2. Build URL format args (only path params)
        url_format_keywords = [
            ast.keyword(arg=name, value=ast.Name(id=name, ctx=ast.Load()))
            for name, _ in path_params
        ]

        # 3. Delegate to self.stream_when_ready(), which polls the 202 to
        #    readiness, follows the redirect, and streams the content to disk
        #    under a single request id (emitting BI events via on_event). It
        #    returns Result[DownloadResult, HttpError].
        body.append(
            ast.Assign(
                targets=[ast.Name(id="result", ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id="self", ctx=ast.Load()),
                        attr="stream_when_ready",
                        ctx=ast.Load(),
                    ),
                    args=[
                        ast.Constant(value="get"),
                        ast.Call(
                            func=ast.Attribute(
                                value=ast.Constant(value=self.config.url_pattern),
                                attr="format",
                                ctx=ast.Load(),
                            ),
                            args=[],
                            keywords=url_format_keywords,
                        ),
                        ast.Name(id="output_path", ctx=ast.Load()),
                    ],
                    keywords=[
                        ast.keyword(
                            arg="params", value=ast.Name(id="params", ctx=ast.Load())
                        ),
                        ast.keyword(
                            arg="chunk_size",
                            value=ast.Name(id="chunk_size", ctx=ast.Load()),
                        ),
                        ast.keyword(
                            arg="progress_callback",
                            value=ast.Name(id="progress_callback", ctx=ast.Load()),
                        ),
                        ast.keyword(
                            arg="timeout", value=ast.Name(id="timeout", ctx=ast.Load())
                        ),
                        ast.keyword(
                            arg="max_wait_seconds",
                            value=ast.Name(id="max_wait_seconds", ctx=ast.Load()),
                        ),
                        ast.keyword(
                            arg="poll_interval",
                            value=ast.Name(id="poll_interval", ctx=ast.Load()),
                        ),
                        ast.keyword(
                            arg="request_id",
                            value=ast.Name(id="request_id", ctx=ast.Load()),
                        ),
                        ast.keyword(
                            arg="on_event",
                            value=ast.Name(id="on_event", ctx=ast.Load()),
                        ),
                    ],
                ),
            )
        )

        # 4. Error check: if is_err(result): return result
        #    The is_err() type guard lets pyright narrow result to the Err
        #    variant here and to Ok[DownloadResult] afterwards.
        body.append(
            ast.If(
                test=ast.Call(
                    func=ast.Name(id="is_err", ctx=ast.Load()),
                    args=[ast.Name(id="result", ctx=ast.Load())],
                    keywords=[],
                ),
                body=[ast.Return(value=ast.Name(id="result", ctx=ast.Load()))],
                orelse=[],
            )
        )

        # 5. Return ResultOk(result.unwrap().path) so the public method keeps
        #    its non-breaking Result[Path, HttpError] signature.
        body.append(
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id="ResultOk", ctx=ast.Load()),
                    args=[
                        ast.Attribute(
                            value=ast.Call(
                                func=ast.Attribute(
                                    value=ast.Name(id="result", ctx=ast.Load()),
                                    attr="unwrap",
                                    ctx=ast.Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr="path",
                            ctx=ast.Load(),
                        )
                    ],
                    keywords=[],
                )
            )
        )

        return body

    def _build_docstring(
        self,
        path_params: list[tuple[str, str]],
        query_params: list[tuple[str, str]],
    ) -> ast.Expr:
        """Build docstring as AST Expr node."""

        # Build sections
        sections = [
            # Summary
            [self.config.docstring],
            # Description
            [
                "Downloads directly to disk using streaming, avoiding loading",
                "the entire file into memory. Ideal for large files (1GB+).",
            ],
            # Args
            ["Args:"]
            + [
                f"    {name} ({type_}): {_get_param_description(name)}"
                for name, type_ in path_params
            ]
            + ["    output_path (Path | str): Where to save the downloaded file."]
            + [
                f"    {name} ({type_}): {_get_param_description(name)}"
                for name, type_ in query_params
            ]
            + [
                f"    chunk_size (int): Bytes per chunk (default: {self.config.default_chunk_size}). Use 64KB+ for faster downloads.",
                "    progress_callback: Optional callback for download progress tracking.",
                "                     Signature: callback(bytes_downloaded: int, total_bytes: int | None)",
                "    timeout: Optional request timeout in seconds. Overrides the instance timeout.",
                "    max_wait_seconds (float): Total wall-clock budget to wait for the",
                "                     download to be prepared server-side (202 polling).",
                "    poll_interval (float | None): If set, overrides the server's Retry-After delay.",
                "    request_id (str | None): Correlation id for the operation; a uuid4 is",
                "                     generated if omitted. Sent on every request and reported in events.",
                "    on_event: Optional callback receiving a DownloadEvent at the started,",
                "                     polling, completed and failed phases (for BI/analytics).",
            ],
            # Returns
            [
                "Returns:",
                "    Result[Path, HttpError]: Ok(Path) on success, Err(HttpError) on failure",
            ],
        ]

        # Flatten sections with blank lines between them
        parts = []
        for i, section in enumerate(sections):
            parts.extend(section)
            if i < len(sections) - 1:  # Add blank line between sections
                parts.append("")

        return ast.Expr(value=ast.Constant(value="\n".join(parts)))

    def _build_return_annotation(self) -> ast.Subscript:
        """Build Result[Path, HttpError] return annotation."""
        return ast.Subscript(
            value=ast.Name(id="Result", ctx=ast.Load()),
            slice=ast.Tuple(
                elts=[
                    ast.Name(id="Path", ctx=ast.Load()),
                    ast.Name(id="HttpError", ctx=ast.Load()),
                ],
                ctx=ast.Load(),
            ),
            ctx=ast.Load(),
        )


def parse_type_annotation(type_str: str) -> ast.expr:
    """
    Parse type annotation string into AST expression.

    Handles common patterns:
    - UUID → ast.Name('UUID')
    - str → ast.Name('str')
    - list[Foo] → ast.Subscript(...)
    - Union[A, B] → ast.BinOp with BitOr
    - None | int → ast.BinOp with BitOr

    Args:
        type_str: Type annotation as string (e.g., 'UUID', 'list[str]')

    Returns:
        AST expression node representing the type
    """
    # Use ast.parse to handle complex type annotations
    # Wrap in a function signature to parse the type annotation
    try:
        module = ast.parse(f"def f(x: {type_str}): pass")
        func = module.body[0]
        if not isinstance(func, ast.FunctionDef):
            return ast.Name(id=type_str, ctx=ast.Load())
        annotation = func.args.args[0].annotation
        if annotation is None:
            return ast.Name(id=type_str, ctx=ast.Load())
        return annotation
    except (SyntaxError, IndexError):
        # Fallback to simple Name node if parsing fails
        return ast.Name(id=type_str, ctx=ast.Load())


def _get_param_description(param_name: str) -> str:
    """Get a generic description for a parameter."""
    descriptions = {
        "contract_id": "The contract ID",
        "order_id": "The order ID",
        "item_id": "The item ID",
        "collections": "Optional subset of collections to download",
        "primary_formats": "Optional file format(s) to download",
    }
    return descriptions.get(param_name, "Parameter")


def generate_streaming_method(config: StreamingEndpointConfig) -> str:
    """
    Generate streaming method code from config using AST.

    Args:
        config: Streaming endpoint configuration

    Returns:
        Generated method code as string
    """
    builder = ASTMethodBuilder(config)
    method_node = builder.build_method()

    # Fix missing line numbers and column offsets
    ast.fix_missing_locations(method_node)

    # Convert AST to code string
    code = ast.unparse(method_node)

    return code


def add_imports_to_ast(
    tree: ast.Module, imports_to_add: dict[str, list[tuple[str, str | None]]]
) -> ast.Module:
    """
    Add missing imports to AST module.

    Args:
        tree: Existing module AST
        imports_to_add: Dict mapping module names to list of (name, alias) tuples
                       e.g., {'pathlib': [('Path', None)],
                              'satvu.result': [('Result', None), ('Ok', 'ResultOk')]}

    Returns:
        Modified AST module with imports added
    """
    # Find where to insert imports (after existing imports)
    insert_idx = 0
    for i, node in enumerate(tree.body):
        if isinstance(node, ast.Import | ast.ImportFrom):
            insert_idx = i + 1

    # Check what imports already exist (including aliases)
    existing_imports: dict[str, set[tuple[str, str | None]]] = {}
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            if node.module not in existing_imports:
                existing_imports[node.module] = set()
            for alias in node.names:
                if alias.name != "*":
                    existing_imports[node.module].add((alias.name, alias.asname))

    # Build new import nodes for missing imports
    new_imports = []
    for module, names_with_aliases in imports_to_add.items():
        existing = existing_imports.get(module, set())
        missing = [
            (name, alias)
            for name, alias in names_with_aliases
            if (name, alias) not in existing
        ]

        if missing:
            # Create ImportFrom node
            import_node = ast.ImportFrom(
                module=module,
                names=[ast.alias(name=name, asname=alias) for name, alias in missing],
                level=0,
            )
            new_imports.append(import_node)

    # Insert new imports
    tree.body[insert_idx:insert_idx] = new_imports

    return tree


def insert_method_after_base(
    tree: ast.Module, base_method: str, new_method_code: str
) -> ast.Module:
    """
    Insert new method after base method in module AST.

    Args:
        tree: Module AST
        base_method: Name of base method to insert after
        new_method_code: Generated method code as string

    Returns:
        Modified AST module with new method inserted
    """
    # Parse the new method code
    new_method_tree = ast.parse(new_method_code)
    new_method_node = new_method_tree.body[0]
    if not isinstance(new_method_node, ast.FunctionDef):
        return tree  # Safety check - should never happen with our generated code

    # Find the class definition (should be first class in module)
    class_node = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_node = node
            break

    if not class_node:
        return tree

    # Find base method in class
    base_method_idx = None
    for i, node in enumerate(class_node.body):
        if isinstance(node, ast.FunctionDef) and node.name == base_method:
            base_method_idx = i
            break

    if base_method_idx is None:
        return tree

    # Insert new method after base method
    class_node.body.insert(base_method_idx + 1, new_method_node)

    return tree
