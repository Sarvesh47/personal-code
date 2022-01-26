from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\\Users\\admin\\Documents\\drivers\\geckodriver.exe")
#driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
best_sellers=driver.find_element(By.LINK_TEXT,'Best Sellers')

driver.execute_script("argument[0].style.border='3px solid red'",best_sellers)
time.sleep(5)