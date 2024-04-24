from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Keep Chrome browser open after program finished
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
test = driver.find_element(By.CSS_SELECTOR, value="#store div")

timeout = time.time() + 10
playing = True

while playing:
    cookie.click()

    if time.time() > timeout:
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        store_items = [item for item in store]
        store_items.reverse()
        for item in store_items:
            if item.get_attribute("class") == "":
                print("click")
                item.click()
                break
        timeout = time.time() + 10


#driver.quit()
