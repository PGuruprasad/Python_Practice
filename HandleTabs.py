from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
TitleFirst=driver.title
driver.find_element(By.ID, "opentab").click()
MultiTabs=driver.window_handles
driver.switch_to.window(MultiTabs[1])
print(driver.title)
driver.close()
driver.switch_to.window(MultiTabs[0])
assert driver.title == TitleFirst
driver.close()
