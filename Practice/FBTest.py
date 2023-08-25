from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser_Opt=webdriver.ChromeOptions()
browser_Opt.add_argument("haedless")
browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=browser_Obj,options=browser_Opt)
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
# userNameValue=driver.find_element(By.ID, "email").text
# print(userNameValue)
userName=driver.find_element(By.ID, "email")
userName.clear()
userName.send_keys("guruprasadpagadala@gmail.com")
userPass=driver.find_element(By.ID, "pass")
userPass.clear()
userPass.send_keys("Ajay@2014")
userPass.send_keys(Keys.ENTER)
time.sleep(5)
