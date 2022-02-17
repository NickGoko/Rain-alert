import requests
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "a43658bab06959323d3134972dc9b7f0"
account_sid = "ACa0e7a944d22458d83d71743970669f1c"
auth_token = "1c25da6967951ff3fbcb0f87c7460154"

MY_LAT = -13.995720
MY_LONG = 33.759820
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "APPID": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(OMW_Endpoint, params=weather_params)

response.raise_for_status()
print(response)
data = response.json()

# print(data)
weather_slice_first_twelve_hours = data["hourly"][0:11]
# print(weather_slice_first_twelve_hours)
hour = data["hourly"][0]["weather"][0]["id"]

will_rain = False
for hour_data in weather_slice_first_twelve_hours:
    condition_code = (hour_data["weather"][0]["id"])
    description_condition = (hour_data["weather"][0]["description"])
    if condition_code <= 700:
        will_rain = True

if will_rain is True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= "Its going to rain, carry your umbrella☂️",
        from_='+19035231427',
        to= "+254702829893"
    )

print(message.status)
