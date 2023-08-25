from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "openwindow").click()
TogleWindow=driver.window_handles
driver.switch_to.window(TogleWindow[1])
print(driver.title)
assert "QAClick Academy" in driver.title
driver.close()
driver.switch_to.window(TogleWindow[0])
print(driver.title)
assert driver.title == "Practice Page"
driver.close()