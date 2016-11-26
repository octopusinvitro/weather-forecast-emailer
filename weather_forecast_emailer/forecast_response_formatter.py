from .forecast_response import ForecastResponse
from .constants import ICON_URL, ICON_EXT
from datetime import datetime


class ForecastResponseFormatter(ForecastResponse):
    def weather_icon(self):
        icon = super(ForecastResponseFormatter, self).weather_icon()
        return ICON_URL + icon + ICON_EXT

    def main_temp(self):
        return self.__format_temp(
            super(ForecastResponseFormatter, self).main_temp())

    def main_temp_min(self):
        return self.__format_temp(
            super(ForecastResponseFormatter, self).main_temp_min())

    def main_temp_max(self):
        return self.__format_temp(
            super(ForecastResponseFormatter, self).main_temp_max())

    def main_pressure(self):
        return self.__append_unit(
            super(ForecastResponseFormatter, self).main_pressure(), ' hpa')

    def main_humidity(self):
        return self.__append_unit(
            super(ForecastResponseFormatter, self).main_humidity(), '%')

    def wind_speed(self):
        return self.__append_unit(
            super(ForecastResponseFormatter, self).wind_speed(), ' m/s')

    def dt(self):
        return datetime.fromtimestamp(
            super(ForecastResponseFormatter, self).dt())

    def sys_sunrise(self):
        return datetime.fromtimestamp(
            super(ForecastResponseFormatter, self).sys_sunrise())

    def sys_sunset(self):
        return datetime.fromtimestamp(
            super(ForecastResponseFormatter, self).sys_sunset())

    def __append_unit(self, item, unit):
        return str(item) + unit

    def __format_temp(self, temperature):
        return self.__append_unit(
            '{0:.2f}'.format(self.__kelvin_to_celsius(temperature)), ' C')

    def __kelvin_to_celsius(self, temperature):
        return temperature - 273.15
