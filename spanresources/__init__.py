import os
import sys

# Add parent directory to path to load env.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load environment variables from env.py, if it exists
if os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'env.py')):
    import env
    print("✅ env.py loaded")
else:
    print("⚠️ env.py NOT found")

# Print to confirm values of environment variables
print("🔑 SECRET_KEY =", os.environ.get("SECRET_KEY"))
print("🔗 DB_URL =", os.environ.get("DB_URL"))

# Initialize Flask app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from sqlalchemy.engine.url import make_url

app = Flask(__name__)

# Initialize CKEditor
ckeditor = CKEditor(app)

# Set up app config
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = (
    os.environ.get("DB_URL") or os.environ.get("DATABASE_URL") or "sqlite:///site.db"
)

# Initialize db and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes after the app is initialized to avoid circular imports
from spanresources import routes  # noqa


