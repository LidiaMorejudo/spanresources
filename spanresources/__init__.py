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
from flask import Flask    # noqa: E402
from flask_sqlalchemy import SQLAlchemy    # noqa: E402
from flask_migrate import Migrate    # noqa: E402
from flask_ckeditor import CKEditor    # noqa: E402
from sqlalchemy.engine.url import make_url    # noqa: E402

app = Flask(__name__)

# Initialize CKEditor
ckeditor = CKEditor(app)

# Set up app config
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default-secret-key")

from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode

db_url = os.environ.get("DB_URL") or os.environ.get("DATABASE_URL")

if db_url:
    url_parts = list(urlparse(db_url))
    query = dict(parse_qsl(url_parts[4]))
    query['sslmode'] = 'require'
    url_parts[4] = urlencode(query)
    db_url = urlunparse(url_parts)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///site.db"

# Initialize db and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes after the app is initialized to avoid circular imports
from spanresources import routes  # noqa
