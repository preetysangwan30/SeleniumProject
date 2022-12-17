from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
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

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
# time.sleep(2)

# now we will write "ber" in the search bar and it will show matching products
# here we will be writing the Xpath for the parent class and loop through
# its child items
time.sleep(3)

products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
assert count > 0

for product in products:
    #element = WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "div/button")))
    # element.click()
    product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

