from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
import time

driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/hris-hr-software-demo/")


print(driver.title)

driver.find_element(By.ID, 'Form_submitForm_FirstName').send_keys("sarvesh")
driver.find_element(By.ID, 'Form_submitForm_LastName').send_keys("pawar")
driver.find_element(By.ID, 'Form_submitForm_Email').send_keys("imsarvesh47@gmail.com")
driver.find_element(By.ID, 'Form_submitForm_Contact').send_keys("9916982217")
driver.find_element(By.ID, 'Form_submitForm_Country').send_keys("india")


time.sleep(5)
