from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.get("https://www.google.com")
acesso = True
if acesso == True:
    driver.close()