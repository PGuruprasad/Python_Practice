from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
ele=driver.find_element(By.XPATH, '//input[@value="radio1"]')
print(ele.is_enabled())
driver.find_element(By.XPATH, '//input[@value="radio1"]').click()
print(ele.is_selected())
print(ele.is_displayed())
drop=driver.find_element(By.ID, "dropdown-class-example")
time.sleep(2)
sdd=Select(drop)
sdd.select_by_index(0)
time.sleep(2)
sdd.select_by_value("option2")
time.sleep(2)
sdd.select_by_visible_text("Option3")
driver.close()