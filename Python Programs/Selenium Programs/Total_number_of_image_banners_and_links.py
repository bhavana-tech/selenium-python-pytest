from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_object)

driver.get("https://www.amazon.com")

#Find teh capcha and enter capcha
# input("Please enter the capcha manually")
# print("Capcha entered, continue with teh scripts")
sliders = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "a-cardui-body")))
print("Total image sliders are", len(sliders))

links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
print("Total links in the page are", len(links))

driver.quit()
