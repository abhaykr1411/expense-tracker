import sqlite3
from werkzeug.security import generate_password_hash

DATABASE_PATH = "spendly.db"


def get_db():
    """
    Get a database connection with row_factory and foreign keys enabled.

    Returns:
        sqlite3.Connection: Database connection object
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """
    Initialize the database by creating tables if they don't exist.
    Safe to call multiple times.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create expenses table with foreign key to users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_db():
    """
    Seed the database with sample data.
    Checks for existing data to prevent duplicates on repeated runs.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Check if users table already has data
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return  # Data already exists, skip seeding

    # Create demo user
    demo_password_hash = generate_password_hash("demo123")
    cursor.execute("""
        INSERT INTO users (name, email, password_hash)
        VALUES (?, ?, ?)
    """, ("Demo User", "demo@spendly.com", demo_password_hash))

    # Get the demo user's ID
    cursor.execute("SELECT id FROM users WHERE email = ?", ("demo@spendly.com",))
    demo_user_id = cursor.fetchone()[0]

    # Sample expenses for the current month (2026-04)
    # Using fixed dates to ensure consistency
    sample_expenses = [
        (demo_user_id, 500.0, "Food", "2026-04-01", "Grocery shopping"),
        (demo_user_id, 200.0, "Transport", "2026-04-03", "Bus pass"),
        (demo_user_id, 1500.0, "Bills", "2026-04-05", "Electricity bill"),
        (demo_user_id, 800.0, "Health", "2026-04-07", "Pharmacy"),
        (demo_user_id, 600.0, "Entertainment", "2026-04-10", "Movie tickets"),
        (demo_user_id, 2000.0, "Shopping", "2026-04-12", "Clothes"),
        (demo_user_id, 300.0, "Food", "2026-04-15", "Restaurant"),
        (demo_user_id, 400.0, "Other", "2026-04-18", "Miscellaneous"),
    ]

    cursor.executemany("""
        INSERT INTO expenses (user_id, amount, category, date, description)
        VALUES (?, ?, ?, ?, ?)
    """, sample_expenses)

    conn.commit()
    conn.close()
