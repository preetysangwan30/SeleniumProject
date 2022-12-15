## Selenium works for HTML pages, but when an alert comes
# it is generally java/javascript, hence there is a separate method
# to handle these alerts, in the alert mode

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Give path to the browser driver
service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

#If the browser closes automatically, below is how to sustain
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#DriverObj is intermediation bw our system and chrome
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Divya")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert # this alert isnow a driver object focused on alerts
# and not on the browser level
alertText = alert.text
print(alertText)
# if your popup has the desired message you would like to accept the alert
assert "Divya" in alertText
alert.accept()
# if you want to dismiss the alert in case it does not have the desired message
# alert.dismiss()