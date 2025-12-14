from cuibuild.swagger import extract_endpoints


def _normalize_function_name(path):
    """
    Derives function name from path.
    Rules:
    - last non-empty segment
    - lowercase
    - replace '-' with '_'
    - prefix '_' if starts with digit
    """
    parts = [p for p in path.split("/") if p]
    name = parts[-1].lower()
    name = name.replace("-", "_")

    if name[0].isdigit():
        name = "_" + name

    return name


def generate_api_js(swagger, tag_filter):
    """
    Generates api.js based on Swagger definition and tag filter.
    """
    endpoints = extract_endpoints(swagger, tag_filter)

    functions = {}

    for path, methods in endpoints.items():
        base_name = _normalize_function_name(path)

        has_get = "get" in methods
        has_post = "post" in methods

        # POST wins base name if conflict exists
        if has_post:
            functions[base_name] = {
                "method": "POST",
                "path": path
            }

        if has_get:
            if has_post:
                get_name = f"get{base_name}"
            else:
                get_name = base_name

            functions[get_name] = {
                "method": "GET",
                "path": path
            }

    # Deterministic ordering
    sorted_functions = dict(sorted(functions.items()))

    return _render_api_js(sorted_functions)


def _render_api_js(functions):
    """
    Renders the final api.js file as a string.
    """
    lines = []

    lines.append("/* ===============================")
    lines.append("   Generated API Client")
    lines.append("   Browser-only, static-safe")
    lines.append("   =============================== */\n")

    lines.append("const API_CONFIG = {")
    lines.append('  BASE_URL: "",')
    lines.append('  HEADERS: {')
    lines.append('    "Content-Type": "application/json"')
    lines.append("  }")
    lines.append("};\n")

    lines.append("async function apiRequest(method, path, payload) {")
    lines.append("  try {")
    lines.append("    const options = {")
    lines.append("      method,")
    lines.append("      headers: API_CONFIG.HEADERS")
    lines.append("    };")
    lines.append("")
    lines.append("    if (method === \"POST\" && payload !== undefined) {")
    lines.append("      options.body = JSON.stringify(payload);")
    lines.append("    }")
    lines.append("")
    lines.append("    const response = await fetch(API_CONFIG.BASE_URL + path, options);")
    lines.append("    const text = await response.text();")
    lines.append("    const data = text ? JSON.parse(text) : null;")
    lines.append("")
    lines.append("    if (!response.ok) {")
    lines.append("      return { error: data || text || response.statusText };")
    lines.append("    }")
    lines.append("")
    lines.append("    return { data };")
    lines.append("  } catch (err) {")
    lines.append("    return { error: err.message };")
    lines.append("  }")
    lines.append("}\n")

    lines.append("const API = {")

    for name, meta in functions.items():
        if meta["method"] == "POST":
            lines.append(
                f"  {name}: (payload) =>"
                f" apiRequest(\"POST\", \"{meta['path']}\", payload),"
            )
        else:
            lines.append(
                f"  {name}: () =>"
                f" apiRequest(\"GET\", \"{meta['path']}\"),"
            )

    # Remove trailing comma
    if functions:
        lines[-1] = lines[-1].rstrip(",")

    lines.append("};")

    return "\n".join(lines)
