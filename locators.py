from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Give path to the browser driver
service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

#If the browser closes automatically, below is how to sustain
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#DriverObj is intermediation bw our system and chrome
driver = webdriver.Chrome(service=service_obj)

#Get to the URL
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Selenium supports locators: ID, Xpath, name, classname, CSSSelector, linkText
#Lets find the email locator to enter the address
driver.find_element(By.NAME, "email").send_keys("pateriya@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#When ID, Name etc is unavailable and you have to create your own attribute
#Custom Xpath Syntax://tagname[@attribute='value'] --> //input[@type='submit']
# CSSSelector: tagname[attribute='value'] --> input[type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Divya Pateriya")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

#To make sure certain message show up on screen after a click ie submit in this case
# In class, there are many classes separated by spaces (when you inspect on the desired popup msg)
msg = driver.find_element(By.CLASS_NAME, "alert-success").text # text property only retrieves the text associated with class
print(msg)

#check if we see "success in message"
assert "Success" in msg