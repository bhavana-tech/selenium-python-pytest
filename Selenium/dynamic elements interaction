import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

try:
    driver.get("https://artoftesting.com/samplesiteforselenium")
    driver.maximize_window()
    time.sleep(10)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//input[@id='male']"))).click()
    print("clicked on radio button")

    # WebDriverWait(driver, 100).until(EC.presence_of_element_located(
    #     (By.CSS_SELECTOR, "input.Automation[value='Automation']"))).click()
    # print("Clicked on Automation")
    checkboxes = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//*[@id='commonWebElements']/form[2]")))
    print("Number of checkbozes are ",len(checkboxes))
    for i in range(len(checkboxes)):
        checkboxes[i].click()

    # driver.execute_script("arguments[0].click()")
    print("clicked on checkbox")
except Exception as e:
    print("Code didnt run")

finally:
    print("finally")
