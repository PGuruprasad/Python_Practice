from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Browser_Obj=Service("C:/Users/DELL/Desktop/Python/Chrome/chromedriver.exe")
driver=webdriver.Chrome(service=Browser_Obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("be")
time.sleep(2)
cartItems=driver.find_elements(By.XPATH, "//div[@class='products']/div")
#itemsList=[]
for item in cartItems:
    #itemsList.append(item.find_element(By.XPATH, "h4").text)
    print(item.find_element(By.XPATH, "h4").text)
    item.find_element(By.XPATH, "div/button").click()
#print("Cart Items : ",itemsList)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# driver.find_element(By.XPATH, "//*[@class='promoCode']").send_keys("rahulshettyacademy")
# driver.find_element(By.XPATH, "//*[@class='promoBtn']").click()
#time.sleep(10)
wait=WebDriverWait(driver,10)
# wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Code applied ..!']")))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
tAmount=driver.find_element(By.XPATH, "//span[@class='totAmt']").text
fAmount=driver.find_element(By.XPATH, "//span[@class='discountAmt']").text
print("Cart Items total price : {} after discount : {}".format(tAmount,fAmount))
assert tAmount>fAmount
driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
countSelect=driver.find_element(By.XPATH, "//select[@style='width: 200px;']")
opt=Select(countSelect)
opt.select_by_visible_text("India")
driver.find_element(By.XPATH, "//input[@class='chkAgree']").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']")
driver.close()