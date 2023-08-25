from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://www.flipkart.com/")
print(type(driver))
driver.maximize_window()
try:
    driver.find_element(By.XPATH, '//button[@class="_2KpZ6l _2doB4z"]').click()
except:
    pass
elem=driver.find_element(By.XPATH, '//input[@type="text"]')
print(elem.get_attribute("placeholder"))
elem.clear()
elem.send_keys("Apple Mobile")
elem.send_keys(Keys.ENTER)
driver.quit()