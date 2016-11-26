from unittest import TestCase

from weather_forecast_emailer import EmailFormatter
from weather_forecast_emailer import ForecastResponseFormatter
from .fake_data import FAKE_RESPONSE


class TestEmailFormatter(TestCase):
    def setUp(self):
        self.formatter = EmailFormatter()
        self.forecast  = ForecastResponseFormatter(FAKE_RESPONSE)

    def test_email_has_a_subject(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertEqual(msg['Subject'], self.formatter.SUBJECT)

    def test_email_has_a_recipient(self):
        recipient = 'recipient@domain.com'
        msg = self.formatter.build_message(recipient, '', self.forecast)
        self.assertEqual(msg['To'], recipient)

    def test_email_includes_text_and_html(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertEqual(len(msg.get_payload()), 2)
        self.assertEqual(msg.get_payload()[0].get_content_type(), 'text/plain')
        self.assertEqual(msg.get_payload()[1].get_content_type(), 'text/html')

    def test_email_includes_the_name(self):
        msg = self.formatter.build_message('', 'name', self.forecast)
        self.assertTrue('name' in msg.as_string())
        self.assertEqual(msg.as_string().count('name'), 2)

    def test_email_includes_the_city_name(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('London' in msg.as_string())
        self.assertEqual(msg.as_string().count('London'), 2)

    def test_email_includes_the_description(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('clear sky' in msg.as_string())
        self.assertEqual(msg.as_string().count('clear sky'), 2)

    def test_email_includes_the_temperature(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('6.70 C' in msg.as_string())
        self.assertEqual(msg.as_string().count('6.70 C'), 2)

    def test_email_includes_the_pressure(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('1023 hpa' in msg.as_string())
        self.assertEqual(msg.as_string().count('1023 hpa'), 2)

    def test_email_includes_the_humidity(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('75%' in msg.as_string())
        self.assertEqual(msg.as_string().count('75%'), 2)

    def test_email_includes_the_wind_speed(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('5.1 m/s' in msg.as_string())
        self.assertEqual(msg.as_string().count('5.1 m/s'), 2)

    def test_email_includes_the_weather_icon_in_html_version(self):
        weather_icon = self.forecast.weather_icon()
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue(weather_icon in msg.get_payload()[1].get_payload())
        self.assertEqual(msg.as_string().count(weather_icon), 1)

    def test_email_includes_header_in_html_version(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('<body>' in msg.get_payload()[1].get_payload())
        self.assertEqual(msg.as_string().count('<body>'), 1)

    def test_email_includes_footer_in_html_version(self):
        msg = self.formatter.build_message('', '', self.forecast)
        self.assertTrue('</body>' in msg.get_payload()[1].get_payload())
        self.assertEqual(msg.as_string().count('</body>'), 1)
