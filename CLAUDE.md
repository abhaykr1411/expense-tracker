# CLAUDE.md

## Project Overview

**Spendly** — a lightweight personal expense tracker built with Flask and SQLite.

---

## Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Flask (Python) + SQLite           |
| Frontend  | Jinja2 templates + Vanilla JS     |
| Styling   | Custom CSS (no framework)         |

---

## Directory Structure

```
expense-tracker/
├── app.py                  # All routes (no blueprints)
├── database/
│   ├── __init__.py         # Empty
│   └── db.py               # get_db, init_db, seed_db
├── templates/
│   ├── base.html           # Shared navbar/footer
│   ├── landing.html        # Hero + features
│   ├── login.html
│   ├── register.html
│   ├── terms.html
│   └── privacy.html
├── static/
│   ├── css/style.css       # All styles
│   └── js/main.js          # All frontend JS
└── requirements.txt
```

**Placement rules:**
- New routes → `app.py` only
- DB logic → `database/db.py` only, never inline in routes
- New pages → new `.html` file extending `base.html`
- Page-specific styles → new `.css` file, not inline `<style>` tags

---

## Code Style

- **Python:** PEP 8, `snake_case` everywhere
- **SQL:** Always use parameterized queries (`?` placeholders) — never f-strings in SQL
- **Templates:** Always use `url_for()` for internal links — never hardcode URLs
- **Routes:** One responsibility per function — fetch data, render template, done
- **Errors:** Use `abort()` for HTTP errors, not bare string returns
- **Python version:** 3.10+ — f-strings and `match` statements are fine

---

## Hard Constraints

- **Flask only** — no FastAPI, no Django
- **SQLite only** — no PostgreSQL, no SQLAlchemy ORM
- **Vanilla JS only** — no React, no jQuery, no npm packages
- **No new pip packages** — stay within `requirements.txt` unless explicitly instructed; keep it in sync if a package is added

---

## Key Behaviors

- **Foreign keys:** SQLite disables FK enforcement by default. `get_db()` must run `PRAGMA foreign_keys = ON` on every connection.
- **`database/db.py` is currently empty** — do not assume any helpers exist until the step that implements them.
- **App runs on port 5001** — do not change this.

---

## Route Status

| Method | Route                   | Status          |
|--------|-------------------------|-----------------|
| GET    | `/`                     | ✅ `landing.html` |
| GET    | `/register`             | ✅ `register.html` |
| GET    | `/login`                | ✅ `login.html` |
| GET    | `/logout`               | 🔲 Step 3       |
| GET    | `/profile`              | 🔲 Step 4       |
| GET    | `/expenses/add`         | 🔲 Step 7       |
| GET    | `/expenses/<id>/edit`   | 🔲 Step 8       |
| GET    | `/expenses/<id>/delete` | 🔲 Step 9       |

> **Rule:** Do not implement a stub route unless the active task explicitly targets that step.

---

## What Not To Do

- ❌ Don't use raw string returns for any route (stub or otherwise)
- ❌ Don't hardcode URLs in templates — use `url_for()`
- ❌ Don't put DB logic inside route functions
- ❌ Don't install new packages without flagging it and updating `requirements.txt`
- ❌ Don't use any JS framework — frontend is intentionally vanilla