from .forecast_response import ForecastResponse


class ForecastResponseError(ForecastResponse):
    def coord_lon(self):
        return 0

    def coord_lat(self):
        return 0

    def weather_id(self):
        return 0

    def weather_main(self):
        return ''

    def weather_description(self):
        return ''

    def weather_icon(self):
        return ''

    def base(self):
        return ''

    def main_temp(self):
        return 0

    def main_pressure(self):
        return 0

    def main_humidity(self):
        return 0

    def main_temp_min(self):
        return 0

    def main_temp_max(self):
        return 0

    def visibility(self):
        return 0

    def wind_speed(self):
        return 0

    def wind_deg(self):
        return 0

    def clouds_all(self):
        return 0

    def dt(self):
        return 0

    def sys_type(self):
        return 0

    def sys_id(self):
        return 0

    def sys_message(self):
        return 0

    def sys_country(self):
        return ''

    def sys_sunrise(self):
        return 0

    def sys_sunset(self):
        return 0

    def id(self):
        return 0

    def name(self):
        return ''

    def cod(self):
        return self.forecast.get('cod', 400)

    def message(self):
        return self.forecast.get('message', 'Not found.')
