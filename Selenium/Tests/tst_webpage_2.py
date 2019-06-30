from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from random import randint
import time

class Base_test():
    """
    Create object for Chrome webdriver then maximalize window and set/load website for test.
    Close browser.
    """
    def setup(self, driver_name):
        " Web Browsers drivers path directory. "
        path_chrome_driver = "C:\Python-geckodriver\chromedriver.exe"
        path_firefox_driver = "C:\Python-geckodriver\geckodriver.exe"
        self.driver_name = driver_name
        print(Colors.bold, Colors.fg.purple)
        print("Web Browser *** {0} *** Web Browser".format(self.driver_name), Colors.reset)

        if self.driver_name == "Chrome":
            " Object from selenium Chrome driver. "
            self.driver = webdriver.Chrome(path_chrome_driver)
        elif self.driver_name == "Firefox":
            " Object from selenium Firefox driver. "
            self.driver = webdriver.Firefox(executable_path = path_firefox_driver)

    def load_main_page(self):
        " Maximize Chrome window. "
        # driver.maximize_window()

        " Go to Webpage. "
        # self.driver.get(r"https://bloodwars.interia.pl")
        self.driver.get(r"http://www.edgewordstraining.co.uk/training-site/")

    def close_browser(self):
        " Close browser"
        self.driver.close()

    def test(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def getTestName(self):
        raise NotImplementedError("Subclass must implement abstract method")

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

class Home(Base_test):
    """
    Check element on a Home screen.
    """
    def test(self, driver_name):
        self.test_page_color()
        self.setup(driver_name)
        self.load_main_page()
        self.navigate()
        self.check_header()
        self.check_part_text()
        self.close_browser()

    def getTestName(self):
        return "'Home Page Test'"

    def test_page_color(self):
        " Set color for Class."
        print(Colors.bold, Colors.fg.blue)
        print("*** Testing Home ***", Colors.reset, end="\n")

    def navigate(self):
        " Check if element is displayed and Navigate to Home screen."
        try:
            home = self.driver.find_element_by_xpath("//span[contains(text(), 'Home')]")
            x = home.is_displayed()
            print("Home is displayed? {0}".format(x))
            home.click()
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("VP FAILED: 'Home' is NOT displayed.", Colors.reset)

    def check_header(self):
        " Check if all text exists. "
        # Expected value:
        self.exp_title = "Automated Tools Test Site"
        try:
            header = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/h1")
            y = header.text
            if y == 'Automated Tools Test Site':
                print("VP PASSED: Text is equal.", "'{1}' = '{0}'".format(y, self.exp_title))
            else:
                print(Colors.fg.red, end="")
                print("VP FAILED: Text is NOT equal.", "Expected = '{1}'", ", actual = '{0}'".format(y, self.exp_title), Colors.reset)
        except NoSuchElementException:
            print("No element displayed.")

    def check_part_text(self):
        " Check if text contain part of text. "
        # Expected value:
        self.exp_part_text = "If you cannot understand my argument"
        try:
            file_text = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/p[1]")
            y = file_text.text
            if self.exp_part_text in y:
                print("VP PASSED: Main text contains part of text: '{0}'".format(self.exp_part_text))
            else:
                print(Colors.fg.red, end="")
                print("VP FAILED: Main text NOT contains part of text:")
                print("Expected = '{1}'", \
                      ", actual = '{0}'".format(y[0:36], self.exp_part_text), Colors.reset)
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("No element displayed.", Colors.reset)

class Basic_HTML(Base_test):
    " Check elements on a Basic HTML screen. "
    def test(self, driver_name):
        self.test_page_color()
        self.setup(driver_name)
        self.load_main_page()
        self.navigate()
        self.check_table()
        # self.check_link()
        self.close_browser()

    def test_page_color(self):
        " Set color for Class."
        print(Colors.bold, Colors.fg.blue)
        print("*** Testing Basic HTML ***", Colors.reset, end="\n")

    def getTestName(self):
        return "'Basic HTML Test'"

    def navigate(self):
        " Check if element is displayed and Navigate to Basic HTML screen."
        try:
            basic_HTML = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/ul/li[2]/a/span")
            x = basic_HTML.is_displayed()
            print("VP PASSED: 'Basic HTML' is displayed? {0}".format(x))
            basic_HTML.click()
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("VP FAILED: 'Basic HTML' is NOT displayed.", Colors.reset)

    def check_table(self):
        " Check elements in a table. "
        # Expected value:
        list_expected = [['Header 1', 'Header 2', 'Header 3'], \
                         ['Value ', 'Value 2', 'Value 3'], \
                         ['Value 1', 'Value 2', 'Value 3 over 2 rows'], \
                         ['Value 1', 'Value 2'], \
                         ['Value over 2 columns', 'Value 3']]
        # print("Expected list:")
        # print(list_expected)
        # print("One cel.")
        # print(list_expected[0][1])
        try:
            table = self.driver.find_element_by_class_name("htmlTable")
            # print("Table:")
            # print(table.text, end="\n\n")
            rows = table.find_elements_by_tag_name("tr")
            i = 0
            list_rows = []
            for row in rows:
                list_cels = []
                print("Row: {0}".format(i + 1))
                # print(row.text)
                column = row.find_elements_by_tag_name("td")
                j = 0
                for col in column:
                    if col.text == list_expected[i][j]:
                        print(" VP PASSED: Col: {0}. Actual: '{1}' = Expected: '{2}'.".format(j, col.text, list_expected[i][j]))
                    else:
                        print(Colors.fg.red, end="")
                        print(" VP FAILED: Col: {0}. Actual: '{1}' = Expected: '{2}'.".format(j, col.text, list_expected[i][j]), Colors.reset)
                    # print("  Col: {0}: {1} ".format(j + 1, col.text))
                    list_cels.append(col.text)
                    # print(list_cels)
                    j += 1
                i += 1
                list_rows.append(list_cels)
            " Check all list in one compare. "
            print("")
            # print("Actual list:")
            # print(list_rows)
            if list_rows == list_expected:
                print("VP PASSED: Values in a Table are the same as expected (Checked list values in one compare).")
            else:
                print(Colors.fg.red, end="")
                print("VP FAILED: Table has different values then expected (Checked list values in one compare).", Colors.reset)
        except NoSuchElementException:
            print("Table is Not displayed.")

    # def check_link(self):
    #     " Check link on a page. "
    #     # link = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/a")
    #     link = self.driver.find_element_by_xpath("//a[@href = 'forms.html']")
    #     link.click()
    #     text = self.driver.find_element_by_xpath("//div[contain(text(), '')")
    #     print(text.text)

class Forms(Base_test):
    """
    Check elements on a Forms screen.
    """
    def test(self, driver_name):
        self.test_page_color()
        self.setup(driver_name)
        self.load_main_page()
        self.navigate()
        raise FileNotFoundError("Wszystko sie zjebalo")
        self.check_something()
        self.close_browser()

    def getTestName(self):
        return "'Forms Test'"

    def test_page_color(self):
        " Set color for Class."
        print(Colors.bold, Colors.fg.blue)
        print("*** Testing Forms ***", Colors.reset, end="\n")

    def navigate(self):
        " Check if element is displayed and Navigate to the Forms page. "
        try:
            forms = self.driver.find_element_by_xpath("//span[contains(text(), 'Forms')]")
            x = forms.is_displayed()
            print("Forms is displayed? {0}".format(x))
            forms.click()
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("VP FAILED: 'Forms' is NOT displayed.", Colors.reset)

    def check_something(self):
        print("'Forms' - Nothing is tested.")

class Dynamic_content(Base_test):
    """
    Check elements on a Dynamic sreen.
    """
    def test(self, driver_name):
        self.test_page_color()
        self.setup(driver_name)
        self.load_main_page()
        self.navigate()
        self.check_something()
        self.close_browser()

    def getTestName(self):
        return "'Dynamic content Test'"

    def test_page_color(self):
        " Set color for Class."
        print(Colors.bold, Colors.fg.blue)
        print("*** Testing Dynamic Content ***", Colors.reset, end="\n")

    def navigate(self):
        " Check if element is displayed and Navigate to the Dynamic Content screen."
        try:
            dynamic = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/ul/li[4]/a/span')
            x = dynamic.is_displayed()
            print("Dynamic is displayed? {0}".format(x))
            dynamic.click()
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("VP FAILED: 'Dynamic content' is NOT displayed.", Colors.reset)

    def check_something(self):
        print("'Dynamic Content' - Nothing is tested.")

class Css_xPath(Base_test):
    """
    Check elements on a CSS/XPath screen.
    """
    def test(self, driver_name):
        self.test_page_color()
        self.setup(driver_name)
        self.load_main_page()
        self.navigate()
        self.check_something()
        self.close_browser()

    def getTestName(self):
        return "'CSS xPath Test'"

    def test_page_color(self):
        " Set color for Class."
        print(Colors.bold, Colors.fg.blue)
        print("*** Testing Css/XPath ***", Colors.reset, end="\n")

    def navigate(self):
        " Check if Css/XPath is displayed and Navigate to the CSS/XPaht screen. "
        try:
            css = self.driver.find_element_by_css_selector('html body div#main-page div#left-column div#menu ul li.last a span')
            x = css.is_displayed()
            print("CSS/XPath is displayed? {0}".format(x))
            css.click()
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("VP FAILED: 'SSS/XPath' is NOT displayed.", Colors.reset)

    def check_something(self):
        print("'CSS/XPath' - Nothing is tested.")



class TestRunner():
    list_web_browsers = ["Chrome", "Firefox"]
    list = []
    def add_test(self, test_class):
        self.list.append(test_class)

    def run_tests(self):
        for driver_name in self.list_web_browsers:
            for test_class in self.list:
                try:
                    test_class.test(driver_name)
                except:
                    print("failed to run test {0}".format(test_class.getTestName()))



testRunner = TestRunner()
testRunner.add_test(Basic_HTML())
testRunner.add_test(Home())
# testRunner.add_test(Forms())
# testRunner.add_test(Dynamic_content())
# testRunner.add_test(Css_xPath())

# Run tests by using method from TestRunner class.
testRunner.run_tests()
