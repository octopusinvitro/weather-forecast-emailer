from unittest import TestCase
from unittest.mock import Mock, patch

from weather_forecast_emailer import BASE_URL, OWM_VERSION
from weather_forecast_emailer import Forecast


class TestForecast(TestCase):
    def setUp(self):
        self.forecast = Forecast('apikey123456')

    @patch('weather_forecast_emailer.forecast.requests.get')
    def test_calls_the_right_url(self, mock_get):
        self.forecast.get_weather_forecast('country_code', 'city_name')
        mock_get.assert_called_once_with(
            BASE_URL + '/data/' + OWM_VERSION +
            '/weather?q=city_name,country_code&appid=apikey123456')

    @patch('weather_forecast_emailer.forecast.requests.get')
    def test_can_pass_no_country(self, mock_get):
        self.forecast.get_weather_forecast('', 'city_name')
        mock_get.assert_called_once_with(
            BASE_URL + '/data/' + OWM_VERSION +
            '/weather?q=city_name&appid=apikey123456')

    @patch('weather_forecast_emailer.forecast.requests.get')
    def test_gets_forecast_when_response_is_ok(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = {"cod": 200}
        response = self.forecast.get_weather_forecast('country_code', 'city_name')
        self.assertEqual(response.cod(), 200)

    @patch('weather_forecast_emailer.forecast.requests.get')
    def test_gets_null_object_if_response_is_ok_but_no_data(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = {"cod": 502}
        response = self.forecast.get_weather_forecast('country_code', 'city_name')
        self.assertEqual(response.cod(), 502)

    @patch('weather_forecast_emailer.forecast.requests.get')
    def test_gets_null_object_if_response_is_not_ok(self, mock_get):
        mock_get.return_value.ok = False
        response = self.forecast.get_weather_forecast('country_code', 'city_name')
        self.assertEqual(response.cod(), 400)
