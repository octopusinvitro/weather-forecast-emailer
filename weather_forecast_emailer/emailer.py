import smtplib
from .constants import MAILHOST, TLS_PORT
from .email_formatter import EmailFormatter


class Emailer:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send_emails(self, emails, forecast):
        server = self.connect()
        self.startTLSencryption(server)
        self.login(server)
        self.sendmail(server, emails, forecast)
        server.quit()

    def connect(self):
        return smtplib.SMTP(MAILHOST, TLS_PORT)

    def startTLSencryption(self, server):
        server.starttls()

    def login(self, server):
        server.login(self.username, self.password)

    def sendmail(self, server, emails, forecast):
        formatter = EmailFormatter()
        for email, name in emails.items():
            message = self.build_message(formatter, email, name, forecast)
            server.sendmail(self.username, email, message)

    def build_message(self, formatter, email, name, forecast):
        return formatter.build_message(email, name, forecast).as_string()
