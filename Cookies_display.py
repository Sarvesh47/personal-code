from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://www.reddit.com/")

cookies=driver.get_cookies()

for cook in cookies:
    print(cook)