from selenium import webdriver
from selenium.webdriver.support.select import Select
import time;

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")

driver.get("https://www.goibibo.com/flights/")

driver.find_element_by_id("gosuggest_inputSrc").send_keys("mum")
time.sleep(2)