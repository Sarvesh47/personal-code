from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
#driver.get("http://www.google.com")
print(driver.title)
import time



driver.implicitly_wait(10)
driver.get("https://formsmarts.com/form-builder-signup")



print(driver.title)




   #sign in
driver.find_element(By.ID, 'fname').send_keys("sarvesh")
driver.find_element(By.ID, 'lname').send_keys("pawar")
driver.find_element(By.ID, 'email').send_keys("sarvesh889@gmail.com")
driver.find_element(By.ID, 'passwd').send_keys("Password@12345")
driver.find_element(By.ID, 'confpasswd').send_keys("Password@12345")



org=driver.find_element(By.ID, 'utyp')
select=Select(org)
select.select_by_index(4)


country=driver.find_element(By.ID, 'country')
select=Select(country)
select.select_by_value("India")


driver.find_element(By.ID, 'submit').click()

