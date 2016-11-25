import requests
from .constants import BASE_URL, OWM_VERSION
from .forecast_response_formatter import ForecastResponseFormatter
from .forecast_response_error import ForecastResponseError


class Forecast:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_forecast(self, country_code, city_name):
        url = self.__makeurl(country_code, city_name)
        return self.__weather_response(url)

    def __makeurl(self, country_code, city_name):
        base_url = BASE_URL + '/data/' + OWM_VERSION + '/weather'
        city     = '?q=' + city_name
        country  = ',' + country_code if country_code else ''
        api_key  = '&appid=' + self.api_key
        return base_url + city + country + api_key

    def __weather_response(self, url):
        response = requests.get(url)
        if response.ok:
            return ForecastResponseFormatter(response.json())
        elif response.ok and response['cod'] != 200:
            return ForecastResponseError(response.json())
        else:
            return ForecastResponseError({})
