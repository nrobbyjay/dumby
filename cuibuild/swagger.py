import json
import urllib.request
import urllib.error


def load_swagger(domain):
    """
    Attempts to load Swagger/OpenAPI JSON from the given domain.
    Tries common Swagger endpoints.
    Returns parsed JSON as dict.
    """
    swagger_urls = [
        f"{domain.rstrip('/')}/swagger.json",
        f"{domain.rstrip('/')}/v2/swagger.json",
        f"{domain.rstrip('/')}/v3/swagger.json",
        f"{domain.rstrip('/')}/openapi.json",
    ]

    last_error = None

    for url in swagger_urls:
        try:
            with urllib.request.urlopen(url) as response:
                if response.status != 200:
                    continue
                data = response.read().decode("utf-8")
                return json.loads(data)
        except (urllib.error.URLError, json.JSONDecodeError) as e:
            last_error = e
            continue

    raise RuntimeError(
        "Failed to load Swagger definition from domain.\n"
        "Tried common paths but none succeeded."
    )


def extract_endpoints(swagger, tag_filter):
    """
    Extracts endpoints from Swagger JSON.
    Only GET and POST are included.
    Filters by exact tag match.
    Returns dict:
      {
        "/path": {
          "get": {...},
          "post": {...}
        }
      }
    """
    paths = swagger.get("paths", {})
    result = {}

    for path, methods in paths.items():
        for method, definition in methods.items():
            method = method.lower()
            if method not in ("get", "post"):
                continue

            tags = definition.get("tags", [])
            if tag_filter and tag_filter not in tags:
                continue

            if path not in result:
                result[path] = {}

            result[path][method] = {
                "tags": tags
            }

    return result
