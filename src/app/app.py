import json
from datetime import date, time, datetime
from logging.config import dictConfig
from flask import Flask, current_app, jsonify
from prometheus_flask_exporter import PrometheusMetrics
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
    app.logger_name = "liturgical-api"

    # Initialise messages
    messages = Messages(from_root("resources", "messages.properties"))

    # Initialise blueprint
    app.register_blueprint(calendar.construct_blueprint(messages))

    # Set short date format when serializing
    # https://github.com/liturgical-app/liturgical-api/issues/27
    app.json.default = lambda obj: obj.isoformat() if isinstance(obj, (date, time, datetime)) else None

    return app


# Create Flask app
app = create_app()

# Initialise metrics
metrics = PrometheusMetrics(app)

@app.route('/healthz', methods=['GET'])
@metrics.do_not_track()
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Only use when running direct
if __name__ == "__main__":
    app.run(
        port=current_app.config["PORT"],
        debug=current_app.config["DEBUG"],
    )
