from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_browser=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=obj_browser)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "name").send_keys("Hello")
driver.find_element(By.ID, "alertbtn").click()
driver.switch_to.alert.accept()
driver.find_element(By.ID, "name").send_keys("Hello")
driver.find_element(By.ID, "confirmbtn").click()
driver.switch_to.alert.dismiss()
driver.close()