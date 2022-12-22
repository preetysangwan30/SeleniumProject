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
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
driver.find_element(By.CLASS_NAME, "blinkingText").click()
windows_opened = driver.window_handles
driver.switch_to.window(windows_opened[1])
email = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text

assert email == "mentor@rahulshettyacademy.com"

driver.close()
driver.switch_to.window(windows_opened[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-danger col-md-12']")))
print(driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']").text)





