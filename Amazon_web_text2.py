from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")

driver.get("https://www.amazon.in/")



driver.find_element(By.LINK_TEXT, 'All').click()
time.sleep(5)
driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
time.sleep()
driver.find_element(By.XPATH,'//*[@id="hmenu-canvas-background"]/div').click()
time.sleep(2)

# driver.find_element(By.LINK_TEXT, 'New Releases').click()
# driver.back()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT, 'Movers and Shakers').click()
# driver.back()
# driver.find_element(By.ID, '').click()By