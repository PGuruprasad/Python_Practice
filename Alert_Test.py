from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.find_element(By.NAME, "enter-name").send_keys("Guru")
driver.find_element(By.XPATH, '//input[@value="Alert"]').click()
driver.switch_to.alert.accept()
time.sleep(5)
driver.find_element(By.NAME, "enter-name").send_keys("Guru")
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(5)
driver.switch_to.alert.dismiss()
driver.close()