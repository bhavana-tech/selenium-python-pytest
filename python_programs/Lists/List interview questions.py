print("1. You have retreived certain elements from web tool in a row using selenium.How will you list them")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_obj = Service(r"C:\Users\Admin\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.moneycontrol.com/")
time.sleep(3)

try:
    element1 = WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located((By.XPATH,'//a[@href="https://www.moneycontrol.com/stocks/marketstats/nsehigh/index.php"]')))
    #driver.execute_script("document.querySelector('a[title=\"52 Week High\"]').click()")
    driver.execute_script("arguments[0].click();", element1)
    print("clicked on element 1")
    list1 = [e.text for e in element1]
    print(list1)

except Exception as e:
    print("Not clicked on element 1")

finally:
    driver.quit()

print("----------------------------------------------------------------------------------")

print("Question 2:How do you handle a list of elements when you want to perform action on each element")
for e in elements:
    e.click()

print("Question 3: How do you verify that the list of elements has specific items")
text=[e.text for e in elements]:
assert 'expected_text' in text

print("Question 4: How to verify id the list of elements contains specific attributes?")
e.text for e in element:
    if specific_attribute in element.getattribute('fe')
        element1.click()

print("Question5: How to sort the list of elements retreived from a web page")
sorted([e.text for e in element]) #This will sort alphabetically

print("Question 6:How can u handle empty lists retreived from a webpage")
driver.find_element(By.ID,"dd")
    if not element:
        print("Return empty list")

print("Question 7: How will you retreive and store the attributes of elements retreived from a webpage")

    test=[e.getattribute('src') for e in element1]

print("Question 8: How to validate if any specific text is present in the list of retreived elements")

if any ('specific_text' in e.text for e in element):
    print("target text found")

print("Question 9: How will u get the index of element retreived from the web page")
elements = driver.find_elements(By.XPATH,'ef')
texts=elem.text for elem in elements
index=texts.index('target text'):
    print(index)

print("Q 10: To insert elements from the last element or last but one element")
list=[1,2,3,4,5,6]
list[-1:-3]=['India','SL','America']
#o/p --> Element will be inserted before -1. 1,2,3,4,5,India,SL,America,6.
# Here -3 doesnt matter.

list1=[1,2,3,4,5,6]
list[-2:-3]=['India','SL','America']
#o/p > Element will be inserted before 5. 1,2,3,4, India,SL,America,5,6.
#Here -3 doesnt mater.

