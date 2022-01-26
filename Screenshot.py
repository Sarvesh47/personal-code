from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")
driver.get("http://www.google.com")
driver.implicitly_wait(10)


driver.get("https://www.reddit.com/")

driver.get_screenshot_as_file('reddit_scr2.png')


