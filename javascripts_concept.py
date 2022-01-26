from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
#driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

best_sellers=driver.find_element(By.LINK_TEXT,'Best Sellers')
driver.execute_script("arguments[0].click()",best_sellers)

title=driver.execute_script("return document.title;") #get a titile
print(title)

driver.execute_script("history.go(0);") #refresh the page

driver.execute_script("alert('hello selenium');")

