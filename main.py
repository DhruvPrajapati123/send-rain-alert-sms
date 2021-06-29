import requests
from twilio.rest import Client

# my2nd_api_id = "75deabc7bfb2aa8301f65a321c029fc6"
# api_key = "bb2b2a25d8e608162039c4183e3a0fb3"
key = "69f04e4613056b159c2761a9d9e664d2"  # Angela API
account_sid = "ACe89ef3ada3b0ff1a0f1b7ba1567efaad"
auth_token = "9a1a6d8282fcb8a0d982efcef85badf8"

parameters = {
    "lat": 56.33,
    "lon": 146.15,
    "appid": key,
    "exclude": "current,minutely,daily",
    "lang": "hi",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]
# print(data["hourly"][0]["weather"]["id"])

will_rain = False

for hour_data in data_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Chata sathe me rakho")
        will_rain = True
if will_rain:
    print("Chata sathe me rakho")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hello mansi",
        from_="+15864602362",
        to="+918200258254"
    )
    print(message.status)
