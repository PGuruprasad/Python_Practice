from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
element_Text=driver.find_element(By.CSS_SELECTOR, ".search-keyword")
input_value="Ber"
driver.execute_script("arguments[0].value=arguments[1];",element_Text,input_value)
time.sleep(5)
driver.close()