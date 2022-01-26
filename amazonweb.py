from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")



print(driver.title)

       #create new ac
#driver.find_element(By.ID, 'ap_customer_name').send_keys("sarvesh")
#driver.find_element(By.ID, 'ap_email').send_keys("imsarvesh67@gmail.com")
#driver.find_element(By.ID, 'ap_phone_number').send_keys("9916986645")
#driver.find_element(By.ID, 'ap_password').send_keys("Sarvesh@123")

   #sign in

driver.find_element(By.LINK_TEXT, 'Sign in').click()
driver.find_element(By.ID, 'ap_email').send_keys("9916987339")
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'ap_password').send_keys("indianarmyfan")

driver.find_element(By.ID, 'signInSubmit').click()

