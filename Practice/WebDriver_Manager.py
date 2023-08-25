from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://pypi.org/project/webdriver-manager/")
driver.maximize_window()
driver.close()