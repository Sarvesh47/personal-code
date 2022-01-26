from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")

driver.get("https://www.globalsqa.com/samplepagetest/")

dropdown = Select(driver.find_element_by_id('g2599-experienceinyears'))
dropdown.select_by_visible_text("1-3")
