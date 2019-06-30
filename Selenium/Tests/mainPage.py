from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

"""
Create object for chrom webdriver then maximalize window and set website for test.
"""
# Chrome driver localization.
path_chrom_driver = "C:\Python-geckodriver\chromedriver.exe"

# Object for Chrom selenium driver.
driver = webdriver.Chrome(path_chrom_driver)

# Maximize Chrom window()
# driver.maximize_window()

# Go to Webpage.
driver.get("http://www.edgewordstraining.co.uk/training-site/")


class Main_page(object):
    """
    Navigate between main screens: 'Home', 'Basic HTML', 'Forms', 'Dynamic Content' and 'CSS/XPath'.
    """

    def __init__(self, navigate):
        self.navigate = navigate

    def navigate_to(self):
        if self.navigate == "Basic HTML":
            basic_HTML = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a/span")
            x = basic_HTML.is_displayed()
            print("Basic HTML is displayed? {0}".format(x))
            basic_HTML.click()
        elif self.navigate == "Home":
            # home = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[1]/a/span")
            home = driver.find_element_by_xpath("//span[contains(text(), 'Home')]")
            x = home.is_displayed()
            print("Home is displayed? {0}".format(x))
            home.click()
        elif self.navigate == "Forms":
            forms = driver.find_element_by_xpath("//span[contains(text(), 'Forms')]")
            x = forms.is_displayed()
            print("Forms is displayed? {0}".format(x))
            forms.click()
        elif self.navigate == "Dynamic Content":
            dynamic = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/ul/li[4]/a/span')
            x = dynamic.is_displayed()
            print("Dynamic is displayed? {0}".format(x))
            dynamic.click()
        elif self.navigate == "CSS/XPath":
            css = driver.find_element_by_css_selector('html body div#main-page div#left-column div#menu ul li.last a span')
            x = css.is_displayed()
            print("CSS/XPath is displayed? {0}".format(x))
            css.click()

    def close_browser(self):
        driver.close()

class Home(object):
    """
    Check element on a Home screen.
    """
    def check_header(self):
        """
        Check if all text exists.
        """
        header = driver.find_element_by_xpath("/html/body/div[2]/div[2]/h1")
        y = header.text
        if y == 'Automated Tools Test Site':
            print("VP PASSED: Text is equal.", "'Automated Tools Test Site' = '{0}'".format(y))
        else:
            print("VP FAILED: Text is NOT equal.", "Expected = 'Automated Tools Test Site'", ", actual = '{0}'".format(y))

    def check_text(self):
        """
        Check if text contain part of text.
        """
        file_text = driver.find_element_by_xpath("/html/body/div[2]/div[2]/p[1]")
        y = file_text.text
        if "If you cannot understand my argument" in y:
            print("VP PASSED: Main text contains part of text: 'If you cannot understand my argument'")
        else:
            print("VP FAILED: Main text NOT contains part of text:")
            print("Expected = 'If you cannot understand my argument'", \
                  ", actual = '{0}'".format(y[0:36]))

# class Basic_HTML():
#
# class Forms():
#
# class Dynamic_content():
#
# class CSS/XPath():