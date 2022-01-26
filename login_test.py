from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://www.webdriveruniversity.com/Contact-Us/contactus.html")


driver.find_element(By.NAME, 'first_name').send_keys('Sarvesh')
driver.find_element(By.NAME, 'last_name').send_keys("Pawar")
#driver.find_element(By.ID, 'continue').click()
#driver.find_element(By.ID, 'ap_password').send_keys("indianarmyfan")

#driver.find_element(By.ID, 'signInSubmit').click()

