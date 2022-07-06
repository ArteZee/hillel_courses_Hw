from unittest import TestCase
from unittest.mock import patch, MagicMock
from artem_task import get_weather, temperature, speed_wind
# Test class checking artem_task.py
class TestWeather(TestCase):

    def test_url(self):
        """
        function checking if website work
        """

        self.assertNotEqual(None, get_weather())
    # mock method which show how work our function without internet connection

    @patch('artem_task.requests')
    def test_temperature_hot(self, requests_mock):
        """
        function check temperature for Hot degrees without website or internet connection
        """
        requests_respone_mock = MagicMock()
        requests_respone_mock.status_code = 200
        requests_respone_mock.json.return_value = {"main": {"temp": 302.15}}

        requests_mock.get.return_value = requests_respone_mock

        self.assertEqual('Hot', temperature("Odesa"))

    def test_temperature_warm(self):
        """
        function check temperature for Warm degrees with website or internet connection
        """
        self.assertEqual("Warm", temperature("London"))
