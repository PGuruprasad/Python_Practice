import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
results =driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(results))
for result in results:
    result.find_element(By.XPATH, 'div/button').click() #Chaining
driver.find_element(By.XPATH, "//img[@alt = 'Cart']").click()
driver.find_element(By.XPATH, '//button[text()="PROCEED TO CHECKOUT"]')
driver.close()