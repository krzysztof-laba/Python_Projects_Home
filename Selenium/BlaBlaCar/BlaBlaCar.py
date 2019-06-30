from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from random import randint
import time
from selenium.common.exceptions import NoSuchElementException
from pynput.keyboard import Key, Controller
import re
import os


#######################################################################################################################

#  Lokalization of chrome driver:
chrome_driver = r"C:\Python-geckodriver\chromedriver.exe"

# Create object for selenium driver:
driver = webdriver.Chrome(chrome_driver)
web_page = "https://www.blablacar.pl/search-car-sharing"


def login(web_site):
    driver.maximize_window()
    driver.get(web_site)


def use_element_class(el_class_name):
    try:
        el = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(By.CLASS_NAME, el_class_name))
        el.click()
    finally:
        print("Element '{0}' not exist.".format(el_class_name))


login(web_page)
use_element_class("flex items-center mx-s large:ml-none large:mr-xl")  # Click login.
use_element_class("jsx-3797635490 kirk-itemChoice-label")  # Click login by FB.
