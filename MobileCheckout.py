# End to end application for product checkout from angular webpage

from selenium import webdriver
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
# Global time out, throughout every code line if the content loads
# selenium will wait max 5 secs for it to appear. If it appears before 5 secs
# code will execute and save rest wait time

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Creating CSS_Selector from attribute href = a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
# mobiles = driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card")

mobiles = driver.find_elements(By.XPATH, "//app-card-list[@class='row']/app-card/div")

for mobile in mobiles:
    if mobile.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
        mobile.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='primary']").click()

assert driver.find_element(By.XPATH, "//div[@class='media']/div/h4").text == "Blackberry" # Applicable when there is only one product in th cart
# Else use the find_elements method and see if the desired product in available in the list

expected_price = "50000"
assert expected_price in driver.find_element(By.XPATH, "//td[@class='text-right']/h3").text
driver.find_element(By.CSS_SELECTOR, "button[class*=success]").click()
driver.find_element(By.CSS_SELECTOR, "input[class*=touched]").send_keys("ind")
# time.sleep(5)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
countries = driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']/label").click()
driver.find_element(By.CSS_SELECTOR, "input[class*=success]").click()
# driver.find_element(By.CSS_SELECTOR, "input[value='submit']").click()

desired_message = "Success"
assert desired_message in driver.find_element(By.CSS_SELECTOR, "div[class*=alert]").text
driver.close()