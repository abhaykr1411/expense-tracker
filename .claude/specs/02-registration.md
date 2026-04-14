---
# Spec: Registration

## Overview

Implement a complete user registration flow that allows new users to create an account. This includes form handling, password hashing, database insertion, and automatic login via session. The registration flow is the first step toward a functional authentication system, enabling users to securely create accounts and begin tracking their personal expenses.

## Depends on

- Step 1 (Database Setup) — the `users` table must exist with proper schema before registration can store data.

## Routes

- **POST `/register`** — Process registration form submission
  - Creates new user with hashed password
  - Validates unique email constraint
  - Sets session for auto-login
  - Returns error messages for validation failures

## Database Changes

No new database changes. Uses existing `users` table schema from Step 1:

| Column | Type | Constraints |
| --- | --- | --- |
| id | INTEGER | Primary key, autoincrement |
| name | TEXT | Not null |
| email | TEXT | Unique, not null |
| password_hash | TEXT | Not null |
| created_at | TEXT | Default CURRENT_TIMESTAMP |

## Templates

- **Create:** None
- **Modify:** None (existing `register.html` template already has the form structure)

## Files to Change

- `app.py` — Add POST handler for `/register` route, replace stub with working implementation
- `database/db.py` — Add `register_user()` function to handle user creation with password hashing

## Files to Create

- None

## New Dependencies

- No new pip packages
- Uses existing: `flask`, `werkzeug.security`

## Rules for Implementation

- **No SQLAlchemy or ORMs** — SQLite with parameterized queries only
- **Password hashing** — Use `generate_password_hash()` from `werkzeug.security`
- **Session management** — Flask's `session` object for auto-login after registration
- **Input validation** — Check for empty fields, email format, minimum password length (8 chars)
- **Error handling** — Return appropriate error messages for:
  - Missing fields
  - Invalid email format
  - Password too short
  - Duplicate email address
- **Parameterized queries only** — Never use f-strings in SQL
- **All templates extend `base.html`** — Existing template structure must be preserved
- **Use `url_for()`** — Never hardcode URLs in templates
- **CSRF protection** — Not required for this step (placeholder for future)

## Definition of Done

- [ ] User can visit `/register` and see the registration form
- [ ] Submitting valid registration data creates a new user in the database
- [ ] Password is properly hashed before storage (not plain text)
- [ ] User is automatically logged in (session set) after successful registration
- [ ] Redirects to dashboard/profile page after registration
- [ ] Error messages display for:
  - Empty fields
  - Invalid email format
  - Password less than 8 characters
  - Duplicate email address
- [ ] App starts without errors after implementation
- [ ] No duplicate users with same email (unique constraint enforced)
