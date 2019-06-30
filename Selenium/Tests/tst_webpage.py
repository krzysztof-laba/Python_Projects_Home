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
    def setup(self):
        " Chrome driver path directory. "
        path_chrome_driver = "C:\Python-geckodriver\chromedriver.exe"

        " Obiect from selenium Chrome driver. "
        self.driver = webdriver.Chrome(path_chrome_driver)

    def load_main_page(self):
        " Maximize Chrome window. "
        # driver.maximize_window()

        " Go to Webpage. "
        # self.driver.get(r"https://bloodwars.interia.pl")
        self.driver.get(r"http://www.edgewordstraining.co.uk/training-site/")

    def close_browser(self):
        " Close browser"
        self.driver.close()

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
    def test(self):
        self.test_page_color()
        self.setup()
        self.load_main_page()
        self.navigate()
        self.check_header()
        self.check_part_text()
        self.close_browser()

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
        # Expected value (text):
        exp_title = "Automated Tools Test Site"
        try:
            header = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/h1")
            y = header.text
            if y == exp_title:
                print("VP PASSED: Text is equal.", "'{1}' = '{0}'".format(y, exp_title))
            else:
                print(Colors.fg.red, end="")
                print("VP FAILED: Text is NOT equal.", "Expected = '{1}'", ", actual = '{0}'".format(y, exp_title), Colors.reset)
        except NoSuchElementException:
            print("No element displayed.")

    def check_part_text(self):
        " Check if text contain part of text. "
        # Expected value (text):
        exp_part_text = "If you cannot understand my argument"
        try:
            file_text = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/p[1]")
            y = file_text.text
            if exp_part_text in y:
                print("VP PASSED: Main text contains part of text: '{0}'".format(exp_part_text))
            else:
                print(Colors.fg.red, end="")
                print("VP FAILED: Main text NOT contains part of text:")
                print("Expected = '{1}'", \
                      ", actual = '{0}'".format(y[0:36], exp_part_text), Colors.reset)
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("No element displayed.", Colors.reset)

class Basic_HTML(Base_test):
    " Check elements on a Basic HTML screen. "
    def test(self):
        self.test_page_color()
        self.setup()
        self.load_main_page()
        self.navigate()
        self.check_table()
        self.check_link()
        self.close_browser()

    def test_page_color(self):
        " Set color for Class."
        print(Colors.bold, Colors.fg.blue)
        print("*** Testing Basic HTML ***", Colors.reset, end="\n")

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
        " Check if element exists. "
        try:
            table = self.driver.find_element_by_class_name("htmlTable")
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("'Table' is Not displayed.", Colors.reset)
            return False
        " Check elements in a table. "
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

    def check_link(self):
        " Check link on a page. "
        print("")
        try:
            # link = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/a")
            link = self.driver.find_element_by_xpath("//a[@href = 'forms.html']")
        except NoSuchElementException:
            print(Colors.fg.red)
            print("There is no 'Link' to check.", Colors.reset)
            return False
        link.click()
        text_page = self.driver.find_element_by_xpath("//p[1]")
        # text = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/p")
        if text_page.text == "This form has an id of theForm.":
            print("VP PASSED: Link probably works. Some text appeared after navigate by 'link'.")
        else:
            print("VP FAILED: Link probably does Not work. Some text does not appear after navigate by 'link'.")

class Forms(Base_test):
    """
    Check elements on a Forms screen.
    """
    def test(self):
        self.test_page_color()
        self.setup()
        self.load_main_page()
        self.navigate()
        self.check_combobox()
        # self.close_browser()

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

    def check_combobox(self):
        try:
            combobox = self.driver.find_element_by_id("select")
        except NoSuchElementException:
            print(Colors.fg.red, end="")
            print("There is no element 'combobox'.")
            return False

        for option in combobox.find_elements_by_tag_name('option'):
            option.click()
            print("")
            # print("Option text: ", option.text)
            if option.text == "Selection One" or option.text == "Selection Two" or option.text == "Selection Three":
                print("VP PASSED: Combobox text is correct: '{0}'.".format(option.text), end="")
            else:
                print(Colors.fg.red, end="")
                print("VP FAILED: Combobox - text unexpected. Actual text: '{0}'.".format(option.text), Colors.reset, end="")





class Dynamic_content(Base_test):
    """
    Check elements on a Dynamic sreen.
    """
    def test(self):
        self.test_page_color()
        self.setup()
        self.load_main_page()
        self.navigate()
        self.check_something()
        self.close_browser()

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
    def test(self):
        self.test_page_color()
        self.setup()
        self.load_main_page()
        self.navigate()
        self.check_something()
        self.close_browser()

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






""" Run test """
site_home = Home()
site_home.test()
site_basic = Basic_HTML()
site_basic.test()
site_forms = Forms()
site_forms.test()
site_dynamic = Dynamic_content()
site_dynamic.test()
site_css = Css_xPath()
site_css.test()