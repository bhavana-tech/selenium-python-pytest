from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_object)

# time.sleep(120)


try:
    driver.get("demo.nopcommerce.com")
    driver.maximize_window()
    time.sleep(60)
    #driver.maximize_window()
    search_input = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-box-text ui-autocomplete-input"))
    )
    print("Search keyword entered")

    driver.execute_script("arguments[0].value = 'Mobile';", search_input)

    print("Search keyword entered")
except Exception as e:
    print("Code dint run")

finally:
    time.sleep(60)
    driver.quit()

#Use of WebElement arguement - Locate the element first and then pass to script.
#The script document.querySelector('input[placeholder="Search store"]').value='Mobile' runs in the browser's context but sometimes
# it may fail to correctly locate the element if the element is not yet fully loaded or interactable.
