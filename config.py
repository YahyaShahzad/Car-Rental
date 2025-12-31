import os
from datetime import timedelta


class Config:
    """Base configuration class with Render production support"""

    # --------------------------------------------------
    # Security
    # --------------------------------------------------
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-secret-key-change-in-production"
    )

    # --------------------------------------------------
    # Database
    # --------------------------------------------------
    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL:
        # Render sometimes provides postgres://
        if DATABASE_URL.startswith("postgres://"):
            DATABASE_URL = DATABASE_URL.replace(
                "postgres://",
                "postgresql+psycopg://",
                1
            )
        # Force psycopg3 even if already postgresql://
        elif DATABASE_URL.startswith("postgresql://"):
            DATABASE_URL = DATABASE_URL.replace(
                "postgresql://",
                "postgresql+psycopg://",
                1
            )

    # Final DB URI (Postgres on Render, SQLite locally)
    SQLALCHEMY_DATABASE_URI = (
        DATABASE_URL or "sqlite:////tmp/car_rental.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------------------
    # Sessions
    # --------------------------------------------------
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    SESSION_COOKIE_SECURE = os.getenv("FLASK_ENV") == "production"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # --------------------------------------------------
    # Flask
    # --------------------------------------------------
    DEBUG = os.getenv("FLASK_ENV") != "production"

    # --------------------------------------------------
    # Business Logic
    # --------------------------------------------------
    MAX_ALLOWED_DISTANCE = 50  # km

    PRICING_TIERS = {
        "economy": 30,
        "luxury": 100,
        "suv": 65,
    }
