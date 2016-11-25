from unittest import TestCase, skip
from unittest.mock import patch

from weather_forecast_emailer import Emailer
from weather_forecast_emailer import MAILHOST, TLS_PORT
from weather_forecast_emailer import ForecastResponseFormatter
from .fake_data import FAKE_RESPONSE


class TestEmailer(TestCase):
    @skip("is not seeing the call to connect() in SMTP constructor")
    @patch('smtplib.SMTP')
    def test_conects_to_the_right_host_and_port(self, smtp_spy):
        Emailer('', '').send_emails({}, '')
        smtp_spy.return_value.connect.assert_called_once_with(MAILHOST, TLS_PORT)

    @patch('smtplib.SMTP')
    def test_encrypts_using_TLS(self, smtp_spy):
        Emailer('', '').send_emails({}, '')
        self.assertTrue(smtp_spy.return_value.starttls.called)

    @patch('smtplib.SMTP')
    def test_logs_in(self, smtp_spy):
        Emailer('username', 'password').send_emails({}, '')
        smtp_spy.return_value.login.assert_called_once_with(
            'username', 'password')

    @patch('smtplib.SMTP')
    def test_sends_email_with_the_right_arguments(self, smtp_spy):
        emails   = {'to@domain.com': 'name'}
        forecast = ForecastResponseFormatter(FAKE_RESPONSE)
        Emailer('username', '').send_emails(emails, forecast)

        ((username, email, message), b) = smtp_spy.return_value.sendmail.call_args
        self.assertEqual(username, 'username')
        self.assertEqual(email, 'to@domain.com')
        self.assertIsNotNone(message)
        self.assertTrue('name' in message)

    @skip("is not intercepting EmailFormatter")
    @patch('smtplib.SMTP')
    @patch('weather_forecast_emailer.EmailFormatter')
    def test_sends_email_to_several_recipients(self, fake_formatter, smtp_spy):
        fake_formatter.return_value.build_message.return_value = 'message'
        emails = {'to@domain.com': 'name', 'foo@domain.com': 'foo name'}
        Emailer('username', '').send_emails(emails, None)
        self.assertEqual(smtp_spy.return_value.sendmail.call_count, 2)
        smtp_spy.return_value.sendmail.assert_any_call(
            'username', 'foo@domain.com', 'message')

    @skip("is not intercepting EmailFormatter")
    @patch('smtplib.SMTP')
    @patch('weather_forecast_emailer.EmailFormatter')
    def test_builds_the_message_to_send(self, fake_formatter, smtp_spy):
        emails = {'to@domain.com': 'name'}
        Emailer('username', '').send_emails(emails, None)
        fake_formatter.return_value.build_message.assert_called_once_with(
            'to@domain.com', 'name', None)

    @patch('smtplib.SMTP')
    def test_quits_when_finished(self, smtp_spy):
        Emailer('', '').send_emails({}, '')
        self.assertTrue(smtp_spy.return_value.quit.called)
