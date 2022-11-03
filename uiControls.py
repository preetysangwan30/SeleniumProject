# In this script we are going to try all the input entering possibilties
# on a website

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

#==================CHECKBOXES====================

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2": #we can use .text() as well
        checkbox.click()
        assert checkbox.is_selected()
    if checkbox.get_attribute("value") == "option1":
        checkbox.click()
        assert checkbox.is_selected()
        
#=================== RADIO BUTTONS ===================

radio_buttons = driver.find_elements(By.CLASS_NAME, "radioButton")
radio_buttons[2].click()
# for button in radio_buttons:
#     if button.get_attribute("value") == "radio1":
#         button.click()
#         assert button.is_selected()
#         break

# ================== DISPLAY BOX==============

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

