from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.maximize_window()
driver.get("https://www.facebook.com/")
userName=driver.find_element(By.XPATH, "//*[contains(@id, 'email')]")
userName.clear()
print(userName.get_attribute("placeholder"))
print(driver.find_element(By.CSS_SELECTOR, "h2[class='_8eso']").text)
userName.send_keys("guruprasadpagadala@gmail.com")
time.sleep(5)
driver.close()