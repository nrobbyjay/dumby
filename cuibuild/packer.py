import os


REQUIRED_FILES = [
    "index.html",
    "style.css",
    "api.js",
    "app.js",
    "AI_CONTEXT.md",
    "UI_REQUIREMENTS.md",
]


def pack_project(output_dir="dist"):
    """
    Flattens scaffold into a single HTML file.
    """
    _validate_required_files()

    index_html = _read_file("index.html")
    style_css = _read_file("style.css")
    api_js = _read_file("api.js")
    app_js = _read_file("app.js")
    ai_context = _read_file("AI_CONTEXT.md")
    ui_requirements = _read_file("UI_REQUIREMENTS.md")

    flattened = _flatten(
        index_html,
        style_css,
        api_js,
        app_js,
        ai_context,
        ui_requirements,
    )

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "index.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(flattened)


def _validate_required_files():
    missing = [f for f in REQUIRED_FILES if not os.path.exists(f)]
    if missing:
        raise RuntimeError(
            "Cannot pack project. Missing required files:\n"
            + "\n".join(f"- {f}" for f in missing)
        )


def _read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _flatten(index_html, style_css, api_js, app_js, ai_context, ui_requirements):
    """
    Produces a single HTML file by inlining assets
    and embedding AI metadata.
    """

    # Remove external CSS link
    index_html = index_html.replace(
        '<link rel="stylesheet" href="style.css">',
        "<style>\n/* ==== style.css ==== */\n"
        + style_css
        + "\n</style>",
    )

    # Remove external JS references
    index_html = index_html.replace(
        '<script src="api.js"></script>',
        "<script>\n/* ==== api.js ==== */\n"
        + api_js
        + "\n</script>",
    )

    index_html = index_html.replace(
        '<script src="app.js"></script>',
        "<script>\n/* ==== app.js ==== */\n"
        + app_js
        + "\n</script>",
    )

    # Embed AI context at top
    ai_block = (
        "<!--\n"
        "================ AI_CONTEXT ================\n"
        + ai_context
        + "\n============================================\n"
        "-->\n\n"
        "<!--\n"
        "============== UI_REQUIREMENTS ==============\n"
        + ui_requirements
        + "\n============================================\n"
        "-->\n\n"
    )

    return ai_block + index_html
