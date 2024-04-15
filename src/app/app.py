import json
from logging.config import dictConfig
from flask import Flask, current_app
from flask_cors import CORS
from from_root import from_root
from src.app.config.config import Config
from src.app.util.messages.messages import Messages
from src.app.calendar import calendar


def create_app():
    # Initialise app
    app = Flask(__name__)
    CORS(app)

    # Initialise config
    config = Config()
    app.config.from_object(config)
    app.app_context().push()

    # Initialise logger
    dictConfig(json.load(open(from_root("app", "config", "logs.json"))))
    app.logger_name = "calendar-api"

    # Initialise messages
    messages = Messages(from_root("resources", "messages.properties"))

    # Initialise blueprint
    app.register_blueprint(calendar.construct_blueprint(messages))

    return app


# Create Flask app
app = create_app()

# Only use when running direct
if __name__ == "__main__":
    app.run(
        port=current_app.config["PORT"],
        debug=current_app.config["DEBUG"],
    )