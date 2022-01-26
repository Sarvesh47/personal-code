from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Documents\\drivers\\chromedriver.exe")



driver.get("https://login.salesforce.com/?locale=in")

#-----------xpath using LinkText-----    //a[text()=''  ]

# driver.find_element_by_xpath("//a[text()='Use Custom Domain']").click()


# -----------xpath Using Parent child traverse mechanism----

print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)

# -----------xpath Using GrandParent child traverse mechanism----

print(driver.find_element_by_xpath("//form[@name='login']/div(1)/label").text)





