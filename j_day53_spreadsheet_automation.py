from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
film_page = response.text

soup = BeautifulSoup(film_page, "html.parser")

all_prices = soup.select(".PropertyCardWrapper__StyledPriceLine")
all_links = soup.select(".StyledPropertyCardDataWrapper a")

all_properties = [link.getText().strip() for link in all_links]
all_prices = [price.getText().replace("/", "+").split("+")[0] for price in all_prices]
all_links = [link.get('href') for link in all_links]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for index in range(len(all_properties)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeHuIzLkcEu0ZAY2fMucIlwgdBpeWdNDsmEpniufjO_C6uj7w/viewform?usp=sf_link")
    time.sleep(2)

    data_input = driver.find_elements(By.CSS_SELECTOR, value=".Xb9hP input")
    # pname = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # pprice = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # plink = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    data_input[0].send_keys(all_properties[index])
    data_input[1].send_keys(all_prices[index])
    data_input[2].send_keys(all_links[index])

    # pname.send_keys(all_properties[index])
    # pprice.send_keys(all_properties[index])
    # plink.send_keys(all_properties[index])

    submit_button.click()

driver.quit()


