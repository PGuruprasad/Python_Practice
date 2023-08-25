from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
options=Select(driver.find_element(By.ID, "dropdown-class-example"))
options.select_by_index(0)
options.select_by_visible_text("Option2")
options.select_by_value("option3")
driver.close()