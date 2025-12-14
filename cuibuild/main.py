import sys

from cuibuild.prompts import (
    prompt_api_domain,
    prompt_swagger_tag,
    prompt_project_intent,
)
from cuibuild.swagger import load_swagger
from cuibuild.api_generator import generate_api_js
from cuibuild.scaffold import generate_scaffold
from cuibuild.packer import pack_project


def print_usage():
    print(
        """
cuibuild - Static UI Builder

Usage:
  cuibuild init     Initialize a new project
  cuibuild pack     Flatten project into single HTML file
"""
    )


def init_command():
    domain = prompt_api_domain()
    swagger = load_swagger(domain)
    tag = prompt_swagger_tag()

    intent = prompt_project_intent()

    # Generate scaffold ONCE
    generate_scaffold(domain, project_intent=intent)

    # Generate api.js
    api_js = generate_api_js(swagger, tag)
    with open("api.js", "w", encoding="utf-8") as f:
        f.write(api_js)

    print("\n✔ Project initialized successfully")


def pack_command():
    pack_project()
    print("\n✔ Project packed into single HTML file")


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        init_command()
    elif command == "pack":
        pack_command()
    else:
        print(f"Unknown command: {command}")
        print_usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
