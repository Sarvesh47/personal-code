from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
driver.implicitly_wait(10)

driver.get('https://www.ibm.com/in-en')
login_ele=driver.find_element(By.CLASS_NAME, 'ibm-profile-link')
act_chains=ActionChains(driver)
act_chains.move_to_element(login_ele).perform()

login=driver.find_element(By.LINK_TEXT,'Log in')
login.click()

time.sleep(3)
driver.quit()