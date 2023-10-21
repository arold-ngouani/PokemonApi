from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.
SECRET_KEY = "THE_MOST_SECRET_KEY_ISlkjnsdfljnslinvesoimsreljnrtblkjndbknljnergkjldfvjhbeviunerfiergiu4587y2h3r089uwev9jn98hf98jv3kjn"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}