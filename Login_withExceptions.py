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

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "username")))

time.sleep(60)
try:
    print("Entering username..")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    print("Username entered")
    #driver.execute_script("document.querySelector('input[placeholder=\"Username\"]').value='Admin'")
except Exception as e:
    print("Username field not found")

try:
    print("Entering password...")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
    #driver.execute_script("document.querySelector('input[placeholder=\"Password\"]').value='admin123'")
    print("Password entered")
except Exception as e:
    print("Password field not found")

try:
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'))).click()
    print("Submit button clicked")
    #driver.execute_script("document.querySelector('button[type=\"submit\"]').click()")
except Exception as e:
    print("Submit button not clickable")

try:
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))).click()
    print("Inside home page")
except Exception as e:
    print("Could not load home page")

finally:
    driver.close()
