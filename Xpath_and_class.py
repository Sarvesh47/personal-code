from selenium import webdriver

driver=webdriver.Firefox(executable_path="C:\\Users\\admin\\Documents\\drivers\\geckodriver.exe")


# driver.minimize_window() //to resize window

driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/with_email")


# $x("//input[@id='user_email']")   //syntax for checking xpath on browser console

driver.find_element_by_xpath("//input[@id='user_email']").send_keys("pawar")


# ----------printing text from webpage using class name----------
print (driver.find_element_by_class_name("heading3").text)


# ----------xpath using class-------    //*[contains(@class,'heading3')]

