[![Build Status](https://travis-ci.org/octopusinvitro/weather-forecast-emailer.svg?branch=master)](https://travis-ci.org/octopusinvitro/weather-forecast-emailer)
[![build status](https://gitlab.com/octopusinvitro/weather-forecast-emailer/badges/master/build.svg)](https://gitlab.com/octopusinvitro/weather-forecast-emailer/commits/master)
[![Coverage Status](https://coveralls.io/repos/github/octopusinvitro/weather-forecast-emailer/badge.svg?branch=master)](https://coveralls.io/github/octopusinvitro/weather-forecast-emailer?branch=master)

# Weather Forecast Emailer

This libray gets the current weather for a city from the [Open Weather Map](openweathermap.or) web API and sends it to a list of emails from a specific Google account.

It is not an exhaustive or complete client wrapper for the OWM service. If that's what you need, [pyown](https://github.com/csparpa/pyowm) offers that functionality. This is just my pet project to practice package creation in Python.


## Usage

Please use responsibly and don't spam people :)

You need four things:

* **An Open Weather Map API key:** The Open Weather Map API needs a valid API key to allow responses. [Create an account](https://home.openweathermap.org/users/sign_up) at the Open Weather Map site and copy your API key.

* **A Gmail username:** This is the username of the Gmail account from where the emails will be sent.

* **A specific app password:** Google needs you to give it permission to send emails in your behalf. Enable 2FA in the previous account and follow the steps in "[Sign in using App Passwords](https://support.google.com/accounts/answer/185833?hl=en)" to get an app password.

* **A list of emails and names:** These can be provided in a file or as a dictionary.

### List of emails and names as a dictionary

You can provide the list of emails and names as a dictionary:

```python
from weather_forecast_emailer import Emailer, Forecast

emails   = {'email1@domain.com': 'Name 1', 'email2@domain.com': 'Name 2'}
forecast = Forecast('YOUR_OWM_API_KEY').get_weather_forecast('uk', 'London')
Emailer('YOUR_USERNAME', 'YOUR_PASSWORD').send_emails(emails, forecast)
```

Replace `uk` and `London` with your country code and city name!

### List of emails and names in a file

You can also provide the list of emails and names in a file and use the `EmailListReader` to get them as a dictionary.

In the file, eparate the email from the name with a comma:

```
# Contents of 'emails.txt'
email1@domain.com, name1
email2@domain.com, name2
```

then you can do:

```python
from weather_forecast_emailer import Emailer, EmailListReader, Forecast

emails   = EmailListReader(open('emails.txt', 'r')).as_dictionary(',')
forecast = Forecast('YOUR_OWM_API_KEY').get_weather_forecast('uk', 'London')
Emailer('YOUR_USERNAME', 'YOUR_PASSWORD').send_emails(emails, forecast)
```

The weather condition codes are explained [here](http://openweathermap.org/weather-conditions).



# Development

## Install

```
pip install .
```


## Install dependencies

```
pip install -r requirements.txt
```


## Run tests

```
python3 -m unittest discover
```


## Publish

```
python3 setup.py register sdist upload
```
