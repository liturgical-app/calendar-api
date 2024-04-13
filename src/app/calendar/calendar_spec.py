import pytest
from liturgical_colour.liturgical import liturgical_colour
from src.app.app import app
from datetime import date


class CalendarSpec:
    client = app.test_client()
    today = date.today()

    @pytest.mark.parametrize("path,date", [
        ("2024-04-13", "2024-04-13"),
        ("today", today)
    ])
    def should_return_liturgical_information_for_a_given_date(self, path, date):
        """ Should return liturgical information for a given date """

        # When
        response = self.client.get(f"/{path}")

        # Then
        assert response.status_code == 200
        assert response.text == liturgical_colour(date)["colour"]

    # TODO :: consider negative/edge cases
