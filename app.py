from flask import Flask, render_template, request, session, redirect, abort
from werkzeug.security import generate_password_hash
from database.db import get_db, init_db, seed_db, register_user

app = Flask(__name__)
app.secret_key = "dev-secret-key"

# Initialize database on startup
with app.app_context():
    init_db()
    seed_db()


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # POST request - process registration form
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    # Validation
    error = None
    if not name:
        error = "Please enter your name"
    elif not email:
        error = "Please enter your email"
    elif "@" not in email or "." not in email:
        error = "Please enter a valid email address"
    elif not password:
        error = "Please enter a password"
    elif len(password) < 8:
        error = "Password must be at least 8 characters"

    if error:
        return render_template("register.html", error=error)

    # Hash password and create user
    password_hash = generate_password_hash(password)
    user_id = register_user(name, email, password_hash)

    if user_id is None:
        return render_template("register.html", error="This email is already registered")

    # Set session and redirect
    session["user_id"] = user_id
    return redirect("/profile")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    return "Logout — coming in Step 3"


@app.route("/profile")
def profile():
    return "Profile page — coming in Step 4"


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
