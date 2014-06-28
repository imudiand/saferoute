import server
from flask import current_app, Flask, Response, request, flash, redirect, url_for, g, session, render_template
from admin.sr.blueprint import sr as sr_blueprint
from admin import settings
from flask.ext.mongoengine import MongoEngine

# Creating a new application
app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    MONGODB_SETTINGS = settings.mongo,
    SECRET_KEY=settings.secret_key,
))

@app.route('/')
def index():
	return render_template('index.html')

# Register Blueprints
app.register_blueprint(sr_blueprint)

def bootstrap():
    db = MongoEngine(app)

def run_debug(host=None, debug=True, user=None, port=3000):
    app.debug = debug
    db = MongoEngine(app)
    app.run(host=host, port=port)

