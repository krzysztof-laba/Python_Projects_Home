from selenium import webdriver
import time


chrome_driver = "C:\Python-geckodriver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver)
driver.maximize_window()

driver.get("http://www.edgewordstraining.co.uk/training-site/index.html")

time.sleep(1)
driver.get("http://www.edgewordstraining.co.uk/training-site/basicHtml.html")
time.sleep(1)
driver.get("http://www.edgewordstraining.co.uk/training-site/forms.html")
time.sleep(1)
driver.get("http://www.edgewordstraining.co.uk/training-site/dynamicContent.html")
time.sleep(1)
driver.get("http://www.edgewordstraining.co.uk/training-site/cssXPath.html")
time.sleep(1)
driver.close()