from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Brow_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Brow_Obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
searchbtn=driver.find_element(By.CLASS_NAME, "search-keyword")
searchbtn.send_keys("Ap")
time.sleep(2)
CartItems=driver.find_elements(By.XPATH, "//div[@class='products']/div")
for i in CartItems:
    print(i.find_element(By.XPATH, "h4").text)
driver.close()