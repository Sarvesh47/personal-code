from selenium import webdriver

driver=webdriver.Firefox(executable_path="C:\\Users\\admin\\Documents\\drivers\\geckodriver.exe")


# driver.minimize_window() //to resize window

driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/with_email")

driver.find_element_by_css_selector("input[name='name']").send_keys('sarvesh')

# -------get text from webpage-------
print(driver.find_element_by_css_selector("[class*='heading3']").text)#using class



# input[name='name'] // CSS creation
# $("input[name='name']") // to check in console
# $("[class*='heading3']") // to check on console using class