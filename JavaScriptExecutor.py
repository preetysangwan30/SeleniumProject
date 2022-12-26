#  Running chrome headless and ignoring SSL certificate errors
#  Here we will perform like scroll the window by executing a javascript with Python-Selenium amd taking SS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Give path to the browser driver
service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

#If the browser closes automatically, below is how to sustain
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# To run chrome in headless mode (back end moded)
ChromeOptionsObj = webdriver.ChromeOptions()
ChromeOptionsObj.add_argument("headless")

# While getting the SSL browser error and you want to proceed anyway for an non-secured connection
ChromeOptionsObj.add_argument("--ignore-certificate-errors")

#DriverObj is intermediation bw our system and chrome
driver = webdriver.Chrome(service=service_obj, options=ChromeOptionsObj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# As selenium itself does not have a method for scrolling down, we'll execute a JavaScript
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("scrolled.png")
