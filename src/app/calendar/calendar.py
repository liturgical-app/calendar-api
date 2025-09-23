import logging
from datetime import date
from flask import Blueprint, jsonify, redirect
from liturgical_calendar.liturgical import liturgical_calendar


# Calendar Logic
def construct_blueprint(messages):
    calendar = Blueprint('calendar', __name__)
    log = logging.getLogger(__name__)

    @calendar.route('/<date>')
    def get_liturgical_info(date):
        """ Retrieve liturgical information for given date """
        log.debug(f"[get_liturgical_info] New request for liturgical info on [{date}]")
        return jsonify(liturgical_calendar(date))

    @calendar.route('/today')
    def get_liturgical_info_today():
        """ Retrieve liturgical information for today's date """
        return get_liturgical_info(date.today())

    @calendar.route('/')
    def home():
        return redirect("/today")

    @calendar.route('/healthz', methods=['GET'])
    @metrics.do_not_track()
    def health_check():
        return jsonify({'status': 'healthy'}), 200

    # Blueprint return
    return calendar
