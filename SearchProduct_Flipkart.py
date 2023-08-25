from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
ele=driver.find_element(By.NAME, "q")
ele.clear()
ele.send_keys("Apple mobile")
ele.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
