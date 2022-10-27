#a,b=5,"Great"
#print("Value of a is {} and b is {}".format(a,b))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#Give path to the browser driver
service_obj = Service("C:/Users/divya/Downloads/chromedriver_win32/chromedriver.exe")

#DriverObj is intermediation bw our system and chrome
driver = webdriver.Chrome(service=service_obj) 

#all actions to be done through the driver obj
driver.get("https://www.youtube.com/") 

#maximize the window
driver.maximize_window()

# get the title of the url
print(driver.title)

# minimize the window
driver.minimize_window()

# Go to a new url
driver.get("https://www.youtube.com/channel/UC6tweGHw_8xAynq8ASYjkQQ")

#Go back
driver.back()

#Go forward a page
driver.forward()

# make sure we landed to the right url before testing by checking curr url
print(driver.current_url) 

#close after everything is done
driver.close()