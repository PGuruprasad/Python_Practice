from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\DELL\\Desktop\\Python\\Chrome\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.gmail.com/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.ID, "identifierId").send_keys("guruprasadpagadala")
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
driver.find_element(By.NAME, "password").send_keys("Guru@1993")
driver.find_element(By.XPATH, '//span[text()="Next"]').click()
driver.find_element(By.XPATH, '//a[@class="gb_d gb_Fa gb_x"]').click()
driver.find_element(By.XPATH, '//div[@class="SedFmc"]').click()
driver.close()
