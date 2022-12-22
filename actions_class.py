# Here we will write operations other than normal clicke
# eg. right click, double click, drag and drop of web element
# hover, click and hold (manily for mobile apps) etc

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

# Global time out, throughout every code line if the content loads
# selenium will wait max 5 secs for it to appear. If it appears before 5 secs
# code will execute and save rest wait time
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver) # creating action object out of driver obj to perform actions like hover over a text
driver.maximize_window()
# action.double_click(driver.find_element(By.ID...) # double click on the web element, provide the web element as an arg here
# action.context_click() # Right click on web elements
# action.click_and_hold() # long press on web element
# action.drag_and_drop() # drag and drop, takes 2 args, first source 2nd destination
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform() # perform() is mandatory for every action we execute
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

# let's reload the page by clicking on the reload optionaction.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

