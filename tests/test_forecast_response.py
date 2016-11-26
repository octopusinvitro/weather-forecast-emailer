from unittest import TestCase

from weather_forecast_emailer import ForecastResponse
from .fake_data import FAKE_RESPONSE


class TestForecastResponse(TestCase):

    def setUp(self):
        self.forecast = ForecastResponse(FAKE_RESPONSE)

    def test_gets_coord_lon(self):
        self.assertEqual(self.forecast.coord_lon(), -0.13)

    def test_gets_coord_lat(self):
        self.assertEqual(self.forecast.coord_lat(), 51.51)

    def test_gets_weather_id(self):
        self.assertEqual(self.forecast.weather_id(), 800)

    def test_gets_weather_main(self):
        self.assertEqual(self.forecast.weather_main(), 'Clear')

    def test_gets_weather_description(self):
        self.assertEqual(self.forecast.weather_description(), 'clear sky')

    def test_gets_weather_icon(self):
        self.assertEqual(self.forecast.weather_icon(), '01n')

    def test_gets_base(self):
        self.assertEqual(self.forecast.base(), 'stations')

    def test_gets_main_temp(self):
        self.assertEqual(self.forecast.main_temp(), 279.85)

    def test_gets_main_pressure(self):
        self.assertEqual(self.forecast.main_pressure(), 1023)

    def test_gets_main_humidity(self):
        self.assertEqual(self.forecast.main_humidity(), 75)

    def test_gets_main_temp_min(self):
        self.assertEqual(self.forecast.main_temp_min(), 278.15)

    def test_gets_main_temp_max(self):
        self.assertEqual(self.forecast.main_temp_max(), 281.15)

    def test_gets_visibility(self):
        self.assertEqual(self.forecast.visibility(), 10000)

    def test_gets_wind_speed(self):
        self.assertEqual(self.forecast.wind_speed(), 5.1)

    def test_gets_wind_deg(self):
        self.assertEqual(self.forecast.wind_deg(), 40)

    def test_gets_clouds_all(self):
        self.assertEqual(self.forecast.clouds_all(), 0)

    def test_gets_dt(self):
        self.assertEqual(self.forecast.dt(), 1480027800)

    def test_gets_sys_type(self):
        self.assertEqual(self.forecast.sys_type(), 1)

    def test_gets_sys_id(self):
        self.assertEqual(self.forecast.sys_id(), 5091)

    def test_gets_sys_message(self):
        self.assertEqual(self.forecast.sys_message(), 0.058)

    def test_gets_sys_country(self):
        self.assertEqual(self.forecast.sys_country(), 'GB')

    def test_gets_sys_sunrise(self):
        self.assertEqual(self.forecast.sys_sunrise(), 1479972930)

    def test_gets_sys_sunset(self):
        self.assertEqual(self.forecast.sys_sunset(), 1480003159)

    def test_gets_id(self):
        self.assertEqual(self.forecast.id(), 2643743)

    def test_gets_name(self):
        self.assertEqual(self.forecast.name(), 'London')

    def test_gets_cod(self):
        self.assertEqual(self.forecast.cod(), 200)
