def prompt_api_domain():
    while True:
        domain = input("Enter API domain (e.g. https://api.example.com): ").strip()
        if domain:
            return domain
        print("API domain cannot be empty.\n")


def prompt_swagger_tag():
    tag = input("Enter Swagger tag to filter endpoints: ").strip()
    return tag


def prompt_project_intent():
    print(
        "\nWhat is this project for?\n"
        "Describe the goal of the UI in your own words.\n"
        "(Press ENTER twice to finish)\n"
    )

    lines = []
    empty_count = 0

    while True:
        line = input()
        if line.strip() == "":
            empty_count += 1
            if empty_count >= 2:
                break
        else:
            empty_count = 0
        lines.append(line)

    intent = "\n".join(lines).strip()
    return intent
