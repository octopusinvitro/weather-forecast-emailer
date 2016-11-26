from setuptools import setup
import unittest


def readme():
    with open('README.md') as f:
        return f.read()


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite  = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(name='weather_forecast_emailer',
      version='0.0.1',
      description='Emails weather forecast from Open Weather Map',
      url='https://github.com/octopusinvitro/weather-forecast-mailer',
      author='Octopus in Vitro',
      author_email=' octopusinvitro@users.noreply.github.com',
      license='MIT',
      packages=['weather_forecast_emailer'],
      install_requires=[
          'requests',
      ],
      tests_require=[
          'mock',
          'coveralls-python',
      ],
      test_suite='setup.my_test_suite',
      zip_safe=False)
