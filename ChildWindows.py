# Let'see how to redirect to the child windows
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

#Give path to the browser driver
service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

#If the browser closes automatically, below is how to sustain
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#DriverObj is intermediation bw our system and chrome
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "opentab").click()
Opened_windows = driver.window_handles # returns of all windows opened with parent at index = 0

driver.switch_to.window(Opened_windows[1])
print(driver.find_element(By.XPATH,"//div[@class='pull-left']/h2").text)
driver.close() # scope of this method is limited to the child tab

driver.switch_to.window(Opened_windows[0])
heading = driver.find_element(By.XPATH, "//h1").text
assert "Practice Page" == heading