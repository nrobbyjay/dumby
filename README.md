# dumby

A contract-driven, AI-safe static UI builder.

dumby is a deliberately strict tool for generating static frontend scaffolds from API definitions, while making the project safe for both humans and AI to work on.

It does not try to be smart.
It tries to be correct, boring, and controllable.

---

## Why dumby exists

AI is great at writing code.
AI is terrible at respecting boundaries.

Most projects break because:
- AI guesses instead of asking
- generators overwrite human work
- intent is lost after the first prompt
- rules live only in someone’s head

dumby fixes this by turning rules and intent into first-class artifacts.

---

## Core ideas

- Capture intent, don’t interpret it
- Generate scaffolds, not applications
- Treat AI as an untrusted actor
- Make constraints explicit and enforceable
- Keep everything static and inspectable

---

## What dumby does

- Generates a minimal static UI scaffold
- Builds a browser-safe API client from Swagger or OpenAPI
- Captures raw project intent verbatim
- Emits an explicit AI contract (AI_CONTEXT.md)
- Allows safe iteration by humans and AI
- Can flatten everything into a single HTML file for delivery

---

## What dumby does NOT do

- Infer payload schemas
- Invent UI behavior
- Add frameworks
- Generate backend code
- Modify generated files silently
- Trust AI without verification

---

## Installation

dumby is a Python CLI tool.

Typical local install during development:

```bash
pip install -e .
```

After installation, the CLI command is available:

```bash
cuibuild
```

---

## CLI usage

### Initialize a project

Run:

```bash
cuibuild init
```

Interactive flow:
1. Enter API domain
2. Swagger or OpenAPI JSON is fetched
3. Choose a Swagger tag to filter endpoints
4. Answer one question only:
   What is this project for?
5. dumby generates the scaffold and API client

All files are written to the current working directory.

---

### Pack (flatten) the project

Run:

```bash
cuibuild pack
```

This command:
- Validates required files
- Inlines CSS and JavaScript
- Embeds AI rules and intent as HTML comments
- Outputs a single self-contained HTML file

Resulting output:

```bash
dist/index.html
```
---

## Generated files

After initialization, dumby generates:

index.html
style.css
app.js
api.js
AI_CONTEXT.md
UI_REQUIREMENTS.md

---

## File responsibilities

| File | Purpose | Editable |
|-----|--------|----------|
| index.html | UI structure | Yes |
| style.css | Styling | Yes |
| app.js | UI logic | Yes |
| api.js | Generated API client | No |
| AI_CONTEXT.md | Hard rules AI must obey | No |
| UI_REQUIREMENTS.md | Raw project intent captured verbatim | No |

Generated files are authoritative and designed to survive regeneration.

---

## AI-first design

### AI_CONTEXT.md

This file is a hard contract.

It tells AI:
- what files exist
- which files may be edited
- which files must never be touched
- what to do if required information is missing

AI is expected to read this file first and refuse to act if rules are violated.

---

### UI_REQUIREMENTS.md

This file contains verbatim human intent captured during initialization.

It is:
- unprocessed
- uninterpreted
- preserved across sessions

AI uses this as guidance, not law.

---

## API client generation

- Based on Swagger or OpenAPI
- GET and POST only
- Endpoints filtered by tag
- Deterministic function naming
- Browser-safe fetch usage
- Always returns either data or error

No schemas. No validation. No inference.

---

## Builder architecture

dumby follows a strict internal rule:

One module equals one file.

The builder is intentionally simple, explicit, and inspectable.
There is no hidden state and no magic.

---

## Who dumby is for

- Engineers building internal tools
- Teams using AI to assist with UI work
- Projects that must survive regeneration
- People who value constraints over cleverness

---

## License

MIT License.

You are free to use, modify, and distribute dumby.

---

## Authorship

This project was designed and authored by a human.

AI tools were used as assistants during development.
All architectural decisions, constraints, and final code are owned by the project author.

---

## Status

Early but functional.
Opinionated by design.
Stable core, evolving edges.

If this resonates with you, you probably already know why it exists.
