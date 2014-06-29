import server
from flask import Flask
from server.saferoute.blueprint import saferoute as saferoute_blueprint
from server import settings
from flask.ext.mongoengine import MongoEngine

# Creating a new application
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    MONGODB_SETTINGS = settings.mongo,
    SECRET_KEY=settings.secret_key,
))

# Register Blueprints
app.register_blueprint(saferoute_blueprint)

def bootstrap():
    db = MongoEngine(app)

def run_debug(host=None, debug=True, user=None, port=5000):
    app.debug = debug
    db = MongoEngine(app)
    app.run(host=host, port=port)

