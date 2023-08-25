from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.ID, "nav-hamburger-menu").click()
driver.find_element(By.XPATH, "//a/div[text()='Fire TV']").click()
driver.find_element(By.XPATH, "//a[text()='Amazon Prime Video']").click()
print(driver.title)
driver.close()