import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_object)

driver.get("https://www.moneycontrol.com/")

element_to_be_clicked = [(By.LINK_TEXT, "News"), (By.LINK_TEXT, "Stocks"),
                         (By.LINK_TEXT, "Franklin Templeton Mutual Fund buys a 0.8% stake in Eris Lifesciences")]

for by_method, value in element_to_be_clicked:
    try:
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((by_method, value))).click()
        print(f"Clicked element with {by_method} = {value}")

        # if (value == "Franklin Templeton Mutual Fund buys a 0.8% stake in Eris Lifesciences"):
        #     time.sleep(50)

        current_url = driver.current_url
        expected_url = "https://www.moneycontrol.com/news/business/markets/franklin-templeton-mutual-fund-buys-a-0-8-stake-in-eris-lifesciences-12769807.html"
        WebDriverWait(driver, 100).until(EC.url_to_be(expected_url))

        if current_url == expected_url:
            print("Successfully navigated to {expected_url}")
    except Exception as e:
        print(f"Not clicked {by_method}={value}")

driver.quit()
print("quitting")
