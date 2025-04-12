from peewee import SqliteDatabase
from pathlib import Path

# Get project root directory and create db path
project_root = Path(__file__).parent.parent.parent
db_path = project_root / "oura.db"

# Create database instance
db = SqliteDatabase(str(db_path))
