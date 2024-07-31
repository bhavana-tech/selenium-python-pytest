from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

service_object = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_object)

driver.get("https://www.moneycontrol.com/stocks/marketstats/index.php")
time.sleep(40)
driver.maximize_window()

text_self = driver.find_element(By.XPATH, "//a[contains(text(),'Hourly Gainers (BSE)')]/self::a").text
print("self node is ", text_self)
print("---------------------------------")

text_parentnode = driver.find_element(By.XPATH, "//a[contains(text(),'Hourly Gainers (BSE)')]/parent::li").text
print("parent node is ", text_parentnode)
print("---------------------------------")

ancestor = driver.find_element(By.XPATH, "//a[contains(text(),'Hourly Gainers (BSE)')]/ancestor::ul").text
print("ancestor node is", ancestor)
print("---------------------------------")

text_child = driver.find_elements(By.XPATH,"//a[contains(text(),'Hourly Gainers (BSE)')]/ancestor::ul/child::td")
print("Child node is ", len(text_child))
print("---------------------------------")

descendant = driver.find_elements(By.XPATH,"//a[contains(text(),'Hourly Gainers (BSE)')]/ancestor::ul/descendant::*")
print("Descendant nodes are", len(descendant))
print("Descendant- select all elements with in the current node")

<html>
  <body>
    <div id="first">
      <p>Paragraph A</p>
      <p>Paragraph A1</p>
    </div>
    <div id="second">
      <p>Paragraph B</p>
    </div>
    <p>Paragraph C</p>
    <div id="third">
      <p>Paragraph D</p>
    </div>
    <p>Paragraph E</p>
    <footer>
      <p>Footer paragraph</p>
    </footer>
    <aside>
      <p>Aside paragraph</p>
    </aside>
  </body>
</html>


# //div[@id='first']/descendant::p --> This gives paragraph A1 ie it selects with in the current node.

# //div[@id='first']/following::p --> This gives paragraph A, paragraph A1 and paragraph B, Paragraph C , Paragraph D,
# Paragraph E, Footer paragraph and Aside paragraph ie it selects with in the current node.


# //div[@id='second']/following-sibling::p --> This gives paragraph C and paragraph  E

# //div[@id='first']/following-sibling::p --> This gives paragraph C and paragraph  E

#//div[@id='first']/preceding::P
