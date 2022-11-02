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

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

#In the dynamic dropdown we'll send "ind" as an input and will wait till all the results show up
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

# find_elements return a list, hence will store into a var
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries)) # printing the nos of outcomes

# Looping through all the country elements and check if it is "India"
for country in countries:
    if country.text == "India":
        country.click()
        break

# check if the clicked element in "India"
# driver.find_element(By.ID,"autosuggest").text() # This will not work, because it works for the data
# already present on the webpage but not for the one entered dynamically
# Use the get_attribute() function to get the value of entered text
country = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(country)
assert country == "India"




