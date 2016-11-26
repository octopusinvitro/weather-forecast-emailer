from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailFormatter:
    SUBJECT = 'Your weather forecast for today!'

    def build_message(self, email, name, forecast):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.SUBJECT
        msg['To'] = email
        text = MIMEText(self.build_text_message(name, forecast), 'plain')
        html = MIMEText(self.build_html_message(name, forecast), 'html')
        msg.attach(text)
        msg.attach(html)
        return msg

    def build_text_message(self, name, forecast):
        message  = self.__greeting(name) + '\n\n'
        message += self.__introduction(forecast.name()) + '\n\n'
        message += self.__build_text_forecast(forecast) + '\n\n\n'
        message += self.__farewell() + '\n\n'
        return message

    def build_html_message(self, name, forecast):
        message  = self.__html_header()
        message += '<p>' + self.__greeting(name) + '</p>'
        message += '<p>' + self.__introduction(forecast.name()) + '</p>'
        message += self.__weather_icon(forecast.weather_icon())
        message += '<ul>' + self.__build_html_forecast(forecast) + '</ul>'
        message += '<p>' + self.__farewell() + '</p>'
        message += self.__html_footer()
        return message

    # Common to text and html
    def __greeting(self, name):
        return 'Hi ' + name + '!'

    def __introduction(self, city):
        return 'This is the weather forecast for the city of ' + city + ' according to the Open Weather Map platform:'

    def __farewell(self):
        return 'Have a nice day!'

    def __forecast_dictionary(self, forecast):
        return {
            'Description': forecast.weather_description(),
            'Temperature': forecast.main_temp(),
            'Pressure':    forecast.main_pressure(),
            'Humidity':    forecast.main_humidity(),
            'Wind speed':  forecast.wind_speed()
        }

    # text and html forecast
    def __build_text_forecast(self, forecast):
        email_body = ''
        for key, value in self.__forecast_dictionary(forecast).items():
            email_body += '\n' + key + ': ' + value
        return email_body

    def __build_html_forecast(self, forecast):
        email_body = ''
        for key, value in self.__forecast_dictionary(forecast).items():
            email_body += '<li><strong>' + key + ':</strong> ' + value + '.</li>'
        return email_body

    # html only
    def __html_header(self):
        return """\
        <html>
            <head></head>
            <body>
        """

    def __weather_icon(self, src):
        return '<img src="' + src + '" width="50" height="50">'

    def __html_footer(self):
        return """\
            </body>
        </html>
        """
