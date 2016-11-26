class ForecastResponse:
    def __init__(self, forecast):
        self.forecast = forecast

    def coord_lon(self):
        return self.forecast['coord']['lon']

    def coord_lat(self):
        return self.forecast['coord']['lat']

    def weather_id(self):
        return self.forecast['weather'][0]['id']

    def weather_main(self):
        return self.forecast['weather'][0]['main']

    def weather_description(self):
        return self.forecast['weather'][0]['description']

    def weather_icon(self):
        return self.forecast['weather'][0]['icon']

    def base(self):
        return self.forecast['base']

    def main_temp(self):
        return self.forecast['main']['temp']

    def main_pressure(self):
        return self.forecast['main']['pressure']

    def main_humidity(self):
        return self.forecast['main']['humidity']

    def main_temp_min(self):
        return self.forecast['main']['temp_min']

    def main_temp_max(self):
        return self.forecast['main']['temp_max']

    def visibility(self):
        return self.forecast['visibility']

    def wind_speed(self):
        return self.forecast['wind']['speed']

    def wind_deg(self):
        return self.forecast['wind']['deg']

    def clouds_all(self):
        return self.forecast['clouds']['all']

    def dt(self):
        return self.forecast['dt']

    def sys_type(self):
        return self.forecast['sys']['type']

    def sys_id(self):
        return self.forecast['sys']['id']

    def sys_message(self):
        return self.forecast['sys']['message']

    def sys_country(self):
        return self.forecast['sys']['country']

    def sys_sunrise(self):
        return self.forecast['sys']['sunrise']

    def sys_sunset(self):
        return self.forecast['sys']['sunset']

    def id(self):
        return self.forecast['id']

    def name(self):
        return self.forecast['name']

    def cod(self):
        return self.forecast['cod']
