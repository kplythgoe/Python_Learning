import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.398640 # Your latitude
MY_LONG = -2.653330 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

my_email = "kieranplythgoe@gmail.com"
password = "dxku jiow ulsw zdgo"

searching = True

while searching:
    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5)  and (MY_LONG - 5 < iss_longitude < MY_LONG + 5):
        if time_now.hour > sunset:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                    msg="Look up at the sky, it's the ISS!")
                time.sleep(60)




