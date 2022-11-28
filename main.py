import os
import requests
from twilio.rest import Client

OWM_API_KEY = os.getenv("OWM_API_KEY")

OWN_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
STOCKHOLM_PARAMETERS = {
    "lat": 59.301213,
    "lon": 18.030364,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


TEST_PARAMETERS = {
    "lat": 33.44,
    "lon": -94.04,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWN_ENDPOINT, params=TEST_PARAMETERS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
            body="Bring an umbrella!",
            from_="+18022789911",
            to="+46734628624"
        )
