from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")

driver.find_element(By.LINK_TEXT,'Best Sellers').click()


driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()