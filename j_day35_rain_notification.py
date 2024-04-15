import requests
import smtplib

my_email = "kieranplythgoe@gmail.com"
password = "***************"

parameters = {
    "lat": 53.398640,
    "lon": -2.653330,
    "appid": "***************************",
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

three_hours_gaps = data["list"]


def will_it_rain():
    for gap in three_hours_gaps:
        for weather in gap["weather"]:
            if weather["id"] < 700:
                return True


will_rain = will_it_rain()
weather_message = ""

if will_rain:
    weather_message = "According to the weather, looks like we're in for some rain today. Grab an umbrella!"
else:
    weather_message = "According to the weather, looks like it isn't going to rain today!"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="kieranplythgoedev@outlook.com",
                        msg=f"Subject:Weather Update\n\n{weather_message}")

