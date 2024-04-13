import logging
from flask import Blueprint, Response


# Calendar Logic
def construct_blueprint(messages):
    calendar = Blueprint('calendar', __name__)
    log = logging.getLogger(__name__)

    @calendar.route("/hello")
    def hello():
        """ Test request (useful for spinning server up after inactivity) """
        return Response("Hello, World!", status=200)

    @calendar.route('/<date>')
    def get_liturgical_info(date):
        """ Retrieve liturgical information for given date """
        log.debug(f"[get_liturgical_info] New request for liturgical info on [{date}]")
        return Response(date, status=200)

    # Blueprint return
    return calendar
