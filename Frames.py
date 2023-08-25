from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.ID, "courses-iframe"))
driver.find_element(By.LINK_TEXT, "Practice").click()
driver.switch_to.default_content()
print(driver.title)
driver.quit()
