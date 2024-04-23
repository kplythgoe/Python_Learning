import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from unidecode import unidecode

MY_EMAIL = "kieranplythgoe@gmail.com"
PASSWORD = "********************"
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Langauge": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")

price = soup.find(name="span", class_="aok-offscreen")
price = float(price.getText().strip().split("$")[1])

name = soup.find(id="productTitle")
name = name.getText().strip()

if price < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="kieranplythgoedev@outlook.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{unidecode(name)} is now on "
                                f"a good deal at ${price}\n{url} ")
