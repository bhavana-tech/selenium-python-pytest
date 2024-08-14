from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

# Specify the path to the ChromeDriver executable
service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#r is a raw string. Why we use r because - in python we normally use "\" as escape character. Since the file path is also
# usses \, it leads to confusion. By prefixing the string with r, u create a raw string literal. so that python
#treats this as literal strings and not as escape characters. Without the r string it could be misinterpreted


@pytest.fixture(scope="module")
def login_github():
    # Initialize WebDriver with the service object
    driver = webdriver.Chrome(service=service_object)
    driver.get("https://github.com/")
    yield driver
    driver.quit()

def test_login_with_validcredentials(login_github):
    # Wait until the login button is clickable and click it
    login_button = WebDriverWait(login_github, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    login_button.click()

    sign_up_for_github = WebDriverWait(login_github, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sign up for GitHub"))
    )
    sign_up_for_github.click()
    # Wait for the username input to be present

