import pytest
from liturgical_calendar.liturgical import liturgical_calendar
from src.app.app import app
from datetime import date


class CalendarSpec:
    client = app.test_client()

    @pytest.mark.parametrize("path,date", [
        ("2024-04-13", "2024-04-13"),
        ("today", date.today())
    ])
    def should_return_liturgical_information_for_a_given_date(self, path, date):
        """ Should return liturgical information for a given date """
        # Given
        info = liturgical_calendar(date)
        info["date"] = "Sun, 14 Apr 2024 00:00:00 GMT"

        # When
        response = self.client.get(f"/{path}")

        # Then
        assert response.status_code == 200
        # assert response.text == liturgical_colour(date) # FixMe

    # TODO :: consider negative/edge cases
