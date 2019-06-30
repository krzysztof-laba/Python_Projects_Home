from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class Base_of_test():
    """
    Settings for base of test.
    Create object for Chrome webdriver.
    Load main page (tested webside) and maximalize window.
    Close browser.
    """

    " Chrome driver path directory. "
    path_chrome_driver = "C:\Python-geckodriver\chromedriver.exe"

    " Obiect from selenium Chrome driver. "
    driver = webdriver.Chrome(path_chrome_driver)

    def load_and_prepare_page(self):
        " Maximize Chrome window. "
        # self.driver.maximize_window()

        " Go to Webpage. "
        # self.driver.get(r"https://bloodwars.interia.pl")
        self.driver.get(r"https://wynagrodzenia.pl/kalkulator-wynagrodzen/przelicz-ponownie")

    def close_advert(self):
        " Switch of an advertisement. "
        try:
            advert = self.driver.find_element_by_class_name("fa fa-times-circle js-exit-modal")
            advert.click()
            print("An advertisement closed.")
        except NoSuchElementException:
            print("No advertisement.")

    def close_browser(self):
        " Close Chrome browser. "
        self.close_browser()

class Colors():
    """
    CLASS FROM INTERNET - I AM NOT AN OWNER.
    """
    '''Colors class:reset all colors with colors.reset; two
        sub classes fg for foreground
        and bg for background; use as colors.subclass.colorname.
        i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
        underline, reverse, strike through,
        and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

class Calculator_test(Base_of_test):
    " Perform tests on a main Webpage: 'Kalkulator wynagrodzeń. "

    def test(self):
        self.load_and_prepare_page()
        self.test_name_of_page()
        self.check_gross()
        self.check_net()
        self.check_if_letters()
        self.check_empty()
        self.check_diff_interest_rate()
        # self.close_browser()

    def test_name_of_page(self):
        print(Colors.fg.blue, end="")
        print("*** Testing 'Calculator salaries' ***", Colors.reset)

    def check_net(self):
        print(Colors.fg.green, end="")
        print("check net income", Colors.reset)
        combobox = self.driver.find_element_by_id("sedlak_calculator_calculateWay")
        combobox.click()
        i = 1
        while i <= 1:
            combobox.send_keys(Keys.ARROW_DOWN)
            i += 1
        combobox.click()
        # self.value_box.send_keys("100")

    def check_gross(self):
        print(Colors.fg.green, end="")
        print("check gross income", Colors.reset)

    def check_if_letters(self):
        print("check letters")

    def check_empty(self):
        print("check empty space")

    def check_diff_interest_rate(self):
        print("check different interest rate")


""" Run tests """
test_calculator_salaries =  Calculator_test()
test_calculator_salaries.test()