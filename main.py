from dynaconf import FlaskDynaconf
from flask import Flask
from flask import jsonify
from flask_mongoengine import MongoEngine

from routes.idea_categorization import idea_categorization
from routes.user import user

app = Flask(__name__)
FlaskDynaconf(app, settings_files=["settings.toml"])
app.config['MONGODB_SETTINGS'] = {
    'db': app.config["MONGODB_SETTINGS_DB"],
    'host': app.config["MONGODB_SETTINGS_HOST_URI"]
}
db = MongoEngine(app)

app.register_blueprint(user)
app.register_blueprint(idea_categorization)
embedding = None


# @app.errorhandler(Exception)
# def exceptions(e):
#     return jsonify({
#         'error': 'Internal Server Error',
#         'error_message': str(e)
#     }), 500


@app.route("/")
def health_check():
    return "OK", 200


if __name__ == '__main__':
    app.run(
        host=app.config.get("HOST"),
        port=app.config.get("PORT"),
        debug=app.config.get("DEBUG"),
    )
