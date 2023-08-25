from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
elem=driver.find_element(By.ID, "name")
elem.send_keys("Python")
driver.find_element(By.ID, "alertbtn").click()
driver.switch_to.alert.accept()
elem=driver.find_element(By.ID, "name")
elem.send_keys("Automation")
driver.find_element(By.ID, "confirmbtn").click()
driver.switch_to.alert.dismiss()
driver.close()
