from unittest import TestCase

from weather_forecast_emailer import ForecastResponseFormatter
from .fake_data import FAKE_RESPONSE


class TestForecastResponseFormatter(TestCase):

    def setUp(self):
        self.forecast = ForecastResponseFormatter(FAKE_RESPONSE)

    def test_formats_weather_icon(self):
        url = 'http://openweathermap.org/img/w/01n.png'
        self.assertEqual(self.forecast.weather_icon(), url)

    def test_formats_main_temp(self):
        self.assertEqual(self.forecast.main_temp(), '6.70 C')

    def test_formats_main_temp_min(self):
        self.assertEqual(self.forecast.main_temp_min(), '5.00 C')

    def test_formats_main_temp_max(self):
        self.assertEqual(self.forecast.main_temp_max(), '8.00 C')

    def test_formats_main_pressure(self):
        self.assertEqual(self.forecast.main_pressure(), '1023 hpa')

    def test_formats_main_humidity(self):
        self.assertEqual(self.forecast.main_humidity(), '75%')

    def test_formats_wind_speed(self):
        self.assertEqual(self.forecast.wind_speed(), '5.1 m/s')

    def test_formats_dt(self):
        self.assertEqual(self.forecast.dt().year, 2016)
        self.assertEqual(self.forecast.dt().month, 11)
        self.assertEqual(self.forecast.dt().day, 24)
        self.assertEqual(self.forecast.dt().hour, 22)
        self.assertEqual(self.forecast.dt().minute, 50)
        self.assertEqual(self.forecast.dt().second, 0)

    def test_formats_sys_sunrise(self):
        self.assertEqual(self.forecast.sys_sunrise().year, 2016)
        self.assertEqual(self.forecast.sys_sunrise().month, 11)
        self.assertEqual(self.forecast.sys_sunrise().day, 24)
        self.assertEqual(self.forecast.sys_sunrise().hour, 7)
        self.assertEqual(self.forecast.sys_sunrise().minute, 35)
        self.assertEqual(self.forecast.sys_sunrise().second, 30)

    def test_formats_sys_sunset(self):
        self.assertEqual(self.forecast.sys_sunset().year, 2016)
        self.assertEqual(self.forecast.sys_sunset().month, 11)
        self.assertEqual(self.forecast.sys_sunset().day, 24)
        self.assertEqual(self.forecast.sys_sunset().hour, 15)
        self.assertEqual(self.forecast.sys_sunset().minute, 59)
        self.assertEqual(self.forecast.sys_sunset().second, 19)
