from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_object)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(60)


username_field = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")
print("Entered username")

password_field = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")
print("Entered password")

submit_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))

submit_button.click()
print("Submit button clicked")

driver.close()
