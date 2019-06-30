from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time


chrome_driver = r"C:\Python-geckodriver\chromedriver.exe"
website = webdriver.Chrome(chrome_driver)
website.get("https://bloodwars.interia.pl")
# website.maximize_window()

try:
    rodo = website.find_element_by_class_name('rodo-popup-agree')
    rodo.click()
except NoSuchElementException:
    print("No rodo.")


def wait_until_page_exists():
    end_time = time.time() + 10
    while True:
        try:
            alexander = website.find_element_by_class_name('me')
            if alexander:
                return alexander
        except NoSuchElementException:
            pass
        if time.time() > end_time:
            print("Wait time finished.")
            break
        time.sleep(0.5)


def login():
    username = website.find_element_by_id('i_login')
    password = website.find_element_by_name('password')
    combobox = website.find_element_by_id('i_realm')
    login = website.find_element_by_xpath('//*[@id="top"]/div/div/form/input[4]')
    username.click()
    username.send_keys("Alexander82")
    password.click()
    password.send_keys("dzieńsądu")
    combobox.click()
    i = 1
    while i <= 2:
        combobox.send_keys(Keys.ARROW_DOWN)
        i += 1
    combobox.click()

    # Login to a BW:
    # login.click()
WebDriverWait(website, 10).until()

login()
wait_until_page_exists()
time.sleep(3)
expeditions = website.find_element_by_xpath("//a[@href='?a=quest']")
expeditions.click()
# website.close()
