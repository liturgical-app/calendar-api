import logging
from datetime import date
from flask import Blueprint, Response, jsonify
from liturgical_colour.liturgical import liturgical_colour


# Calendar Logic
def construct_blueprint(messages):
    calendar = Blueprint('calendar', __name__)
    log = logging.getLogger(__name__)

    @calendar.route('/<date>')
    def get_liturgical_info(date):
        """ Retrieve liturgical information for given date """
        log.debug(f"[get_liturgical_info] New request for liturgical info on [{date}]")
        return jsonify(liturgical_colour(date))

    @calendar.route('/today')
    def get_liturgical_info_today():
        """ Retrieve liturgical information for today's date """
        return get_liturgical_info(date.today())

    # Blueprint return
    return calendar
