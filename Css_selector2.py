from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")



driver.get("https://login.salesforce.com/?locale=in")

driver.find_element_by_css_selector("#username").send_keys("sarvesh") #//using ID-CSS-selector

driver.find_element_by_css_selector(".password").send_keys("sarvesh@123") #//using Class-CSS-selector

driver.find_element_by_css_selector(".password").clear()