from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
element = driver.find_element(By.TAG_NAME, 'label')
print(element.text)
RadioButton=driver.find_element(By.XPATH, "//input[@value='radio1']")
print(RadioButton.is_selected())
driver.close()