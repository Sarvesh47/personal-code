from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
print(driver.title)
