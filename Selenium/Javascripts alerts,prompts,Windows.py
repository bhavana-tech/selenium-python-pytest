How do you handle alerts and pop-ups in Selenium Python using pytest.explain using example.. 

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def browser():
    """Setup and teardown for the browser session."""
    service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_handle_alert(browser):
    """Test case to handle a JavaScript alert pop-up."""
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click the button that triggers a JS Alert
    alert_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']"))
    )
    alert_button.click()

    # Switch to the alert and accept it
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert "I am a JS Alert" in alert.text, "Alert text did not match!"
    alert.accept()  # Accepts the alert

    print("Alert handled successfully!")

def test_handle_confirm_alert(browser):
    """Test case to handle a confirmation alert pop-up."""
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click the button that triggers a JS Confirm Alert
    confirm_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']"))
    )
    confirm_button.click()

    # Switch to the alert and dismiss it
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert "I am a JS Confirm" in alert.text, "Confirm Alert text did not match!"
    alert.dismiss()  # Cancels the alert

    print("Confirmation alert dismissed successfully!")

def test_handle_prompt_alert(browser):
    """Test case to handle a JavaScript prompt pop-up."""
    browser.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click the button that triggers a JS Prompt Alert
    prompt_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Prompt']"))
    )
    prompt_button.click()

    # Switch to the alert and enter text
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert "I am a JS prompt" in alert.text, "Prompt Alert text did not match!"
    alert.send_keys("Hello Selenium!")  # Enter text
    alert.accept()  # Accept the alert

    print("Prompt alert handled successfully!")

