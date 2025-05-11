import os

if os.path.exists("env.py"):
    import env
    print("✅ env.py loaded")
else:
    print("⚠️ env.py NOT found")

# Print to confirm values
print("🔑 SECRET_KEY =", os.environ.get("SECRET_KEY"))
print("🔗 DB_URL =", os.environ.get("DB_URL"))


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from sqlalchemy.engine.url import make_url

app = Flask(__name__)
ckeditor = CKEditor(app)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "default-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL") or "sqlite:///site.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from spanresources import routes  # noqa

