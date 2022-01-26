from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
print(driver.title)
import time

driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")


driver.find_element(By.NAME, 'proceed').click()
time.sleep(5)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
time.sleep(5)
alert.send_keys('hello mayur topper')
driver.switch_to.default_content()
time.sleep(5)
#alert.dismiss()
