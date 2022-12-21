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

driver.implicitly_wait(2)
# Global time out, throughout every code line if the content loads
# selenium will wait max 5 secs for it to appear. If it appears before 5 secs
# code will execute and save rest wait time

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# now we will write "ber" in the search bar and it will show matching products
# here we will be writing the Xpath for the parent class and loop through
# its child items
time.sleep(3) # Need to include sleep() even though we have an implicit wait is because
# find_elements() is the only exception when implicit wait results into an error
# because at first the list is empty means nothing has been displayed

products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
assert count > 0
list = []
for product in products:
    item = product.find_element(By.XPATH, "h4").text # fetching the name of items showing up
    list.append(item)
    product.find_element(By.XPATH, "div/button").click() # clicking on add to cart button
    
expected_products = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

assert list == expected_products

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10) # max time for explicit wait
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# explicit wait are only applicable fot mentioned CSS_Selector because explicit waits are not scoped globally
# but applicable only for components which takes time to load like promo code applied and its loading time to search for its validity
promo_message = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
assert promo_message == "Code applied ..!"

# checking if the sum of all products is the total amount to be paid
prices = driver.find_elements(By.XPATH, "//div[@class='products']/table/tbody/tr/td[5]")
# prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    print(price.text)
    sum = sum + int(price.text)

print(sum)
total_price = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert int(sum) == int(total_price)
disc_price = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert disc_price < total_price
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()