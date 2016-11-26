from unittest import TestCase

from weather_forecast_emailer import ForecastResponseError


class TestForecastResponseError(TestCase):
    def setUp(self):
        self.forecast = ForecastResponseError({"cod": 401, "message": "Error."})

    def test_gets_coord_lon(self):
        self.assertEqual(self.forecast.coord_lon(), 0)

    def test_gets_coord_lat(self):
        self.assertEqual(self.forecast.coord_lat(), 0)

    def test_gets_weather_id(self):
        self.assertEqual(self.forecast.weather_id(), 0)

    def test_gets_weather_main(self):
        self.assertEqual(self.forecast.weather_main(), '')

    def test_gets_weather_description(self):
        self.assertEqual(self.forecast.weather_description(), '')

    def test_gets_weather_icon(self):
        self.assertEqual(self.forecast.weather_icon(), '')

    def test_gets_base(self):
        self.assertEqual(self.forecast.base(), '')

    def test_gets_main_temp(self):
        self.assertEqual(self.forecast.main_temp(), 0)

    def test_gets_main_pressure(self):
        self.assertEqual(self.forecast.main_pressure(), 0)

    def test_gets_main_humidity(self):
        self.assertEqual(self.forecast.main_humidity(), 0)

    def test_gets_main_temp_min(self):
        self.assertEqual(self.forecast.main_temp_min(), 0)

    def test_gets_main_temp_max(self):
        self.assertEqual(self.forecast.main_temp_max(), 0)

    def test_gets_visibility(self):
        self.assertEqual(self.forecast.visibility(), 0)

    def test_gets_wind_speed(self):
        self.assertEqual(self.forecast.wind_speed(), 0)

    def test_gets_wind_deg(self):
        self.assertEqual(self.forecast.wind_deg(), 0)

    def test_gets_clouds_all(self):
        self.assertEqual(self.forecast.clouds_all(), 0)

    def test_gets_dt(self):
        self.assertEqual(self.forecast.dt(), 0)

    def test_gets_sys_type(self):
        self.assertEqual(self.forecast.sys_type(), 0)

    def test_gets_sys_id(self):
        self.assertEqual(self.forecast.sys_id(), 0)

    def test_gets_sys_message(self):
        self.assertEqual(self.forecast.sys_message(), 0)

    def test_gets_sys_country(self):
        self.assertEqual(self.forecast.sys_country(), '')

    def test_gets_sys_sunrise(self):
        self.assertEqual(self.forecast.sys_sunrise(), 0)

    def test_gets_sys_sunset(self):
        self.assertEqual(self.forecast.sys_sunset(), 0)

    def test_gets_id(self):
        self.assertEqual(self.forecast.id(), 0)

    def test_gets_name(self):
        self.assertEqual(self.forecast.name(), '')

    def test_gets_cod(self):
        self.assertEqual(self.forecast.cod(), 401)

    def test_gets_message(self):
        self.assertEqual(self.forecast.message(), 'Error.')

    def test_gets_cod_when_response_is_empty(self):
        self.forecast = ForecastResponseError({})
        self.assertEqual(self.forecast.cod(), 400)

    def test_gets_message_when_response_is_empty(self):
        self.forecast = ForecastResponseError({})
        self.assertEqual(self.forecast.message(), 'Not found.')
