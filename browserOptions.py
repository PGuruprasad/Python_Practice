from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options1=webdriver.ChromeOptions()
options1.add_argument("headless")
Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj,options=options1)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.facebook.com/")
userName=driver.find_element(By.ID, "email")
print(userName.get_attribute("name"))
print(type(driver))
print(driver.title)
driver.close()