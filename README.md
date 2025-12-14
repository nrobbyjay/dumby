# dumby

> **A contract-driven, AI-safe static UI builder.**

**dumby** is a deliberately strict tool for generating static frontend scaffolds from API definitions, while making the project **safe for both humans and AI to work on**.

It does not try to be smart.  
It tries to be **correct, boring, and controllable**.

---

## Why dumby exists

AI is great at writing code.  
AI is terrible at respecting boundaries.

Most projects break because:
- AI guesses instead of asking
- generators overwrite human work
- intent is lost after the first prompt
- rules live only in someone’s head

**dumby fixes this by turning rules and intent into first-class artifacts.**

---

## Core ideas

- **Capture intent, don’t interpret it**
- **Generate scaffolds, not applications**
- **Treat AI as an untrusted actor**
- **Make constraints explicit and enforceable**
- **Keep everything static and inspectable**

---

## What dumby does

- Generates a minimal static UI scaffold
- Builds a browser-safe API client from Swagger/OpenAPI
- Captures raw project intent verbatim
- Emits an explicit AI contract (`AI_CONTEXT.md`)
- Allows safe iteration by humans *and* AI
- Can flatten everything into a single HTML file for delivery

---

## What dumby does NOT do

- ❌ Infer payload schemas
- ❌ Invent UI behavior
- ❌ Add frameworks
- ❌ Generate backend code
- ❌ Modify generated files silently
- ❌ Trust AI without verification

---

## Installation

Local / editable install (recommended):

```bash
pip install -e .
