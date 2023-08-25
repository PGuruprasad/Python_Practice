import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Top")).click().perform()
time.sleep(5)
driver.close()