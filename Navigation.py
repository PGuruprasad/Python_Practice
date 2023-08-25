from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://www.w3schools.com/")
driver.refresh()
driver.get("https://www.flipkart.com/")
driver.back()
time.sleep(2)
print(driver.title)
driver.forward()
time.sleep(2)
print(driver.title)
driver.close()