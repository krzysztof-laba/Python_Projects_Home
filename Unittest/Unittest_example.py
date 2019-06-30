import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestSalaryCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Avoid running this class.
        """
        if cls is TestSalaryCalculator:
            raise unittest.SkipTest("Base class")
        super().setUpClass()

    """
    Checking web application 'Salary Calculator'.
    """

    page_url = r"https://wynagrodzenia.pl/kalkulator-wynagrodzen"
    gross_net_combobox_id = "sedlak_calculator_calculateWay"
    value_text_id = "sedlak_calculator_earnings"
    year_combobox_id = "sedlak_calculator_year"
    interest_rate_id = "work_accidentPercent"
    evaluate_button_id = "sedlak_calculator_save"
    advert_css_class_name = "fa fa-times-circle js-exit-modal"
    invalid_value_css_class_name = "invalid error-empty"
    private_policy_css_class_name = "js-accept"
    validation_error_xpath = "//em[contains(@class, '{0}')]".format(invalid_value_css_class_name)
    company_private_selection_class_names = "side js-side right"
    company_private_selection_class_name_xpath = "//div[contains(@class, '{0}')]".format(company_private_selection_class_names)
    net_value_css_class_name = "col-md-3 col-sm-6"
    net_value_number_xpath = "//div[contains(@class, '{0}')]/span[1]".format(net_value_css_class_name)
    net_value_text_xpath = "//div[contains(@class, '{0}')]/span[2]".format(net_value_css_class_name)
    advertisement_css_class_names = "fa fa-times-circle js-exit-modal"
    advertisement_xpath = "//i[contains(@class, '{0}')]".format(advertisement_css_class_names)
    gross_value_css_class_name = "col-md-3 col-sm-6"
    gross_value_number_xpath = "(//div[contains(@class, '{0}')])[2]/span[1]".format(gross_value_css_class_name)
    gross_value_text_xpath = "(//div[contains(@class, '{0}')])[2]/span[2]".format(gross_value_css_class_name)

    def get_driver(self):
        raise NotImplementedError("abstract method")

    @classmethod
    def tearDownClass(cls):
        cls.get_driver(cls).close()

    def setUp(self):
        print("")
        print("Prepare page.")
        self.get_driver().maximize_window()
        self.get_driver().get(self.page_url)
        try:
            self.get_driver().find_element_by_class_name(self.private_policy_css_class_name).click()
            print("Private policy clicked.")
        except ElementNotVisibleException:
            print("Private policy already clicked.")

    def test_value_text_validation(self):
        """
        Test checks validation when no number value is set to evaluate.
        """
        print("*** Test value text validation ***")
        value_text = self.get_driver().find_element_by_id(self.value_text_id)
        value_text.click()
        value_text.send_keys("qwerty")
        evaluate = self.move_to_element(self.evaluate_button_id)
        evaluate.click()
        try:
            validation_error_elem = self.get_driver().find_element_by_xpath(self.validation_error_xpath)
        except NoSuchElementException as exception:
            print("Failed. No invalid value element.")
            raise exception
        self.assertEqual(validation_error_elem.text, "Podaj poprawną kwotę zarobków")

    def test_net_salary_calculation(self):
        """
        Test checks net and gross salary evaluation when proper value is set to 'Your salary'.
        """
        print("*** Test net salary calculation ****")
        combobox = self.get_driver().find_element_by_id(self.gross_net_combobox_id)
        combobox.click()
        i = 1
        while i <= 1:
            combobox.send_keys(Keys.ARROW_DOWN)
            i += 1
        combobox.click()
        value_text = self.get_driver().find_element_by_id(self.value_text_id)
        value_text.click()
        value_text.send_keys("5500")
        evaluate = self.move_to_element(self.evaluate_button_id)
        evaluate.click()
        self.close_company_private_selection()
        self.close_advertisement()

        # Check pass condition.
        net_value_number = self.get_driver().find_element_by_xpath(self.net_value_number_xpath)
        self.assertEqual(net_value_number.text, "5 500,00 PLN")
        net_value_text = self.get_driver().find_element_by_xpath(self.net_value_text_xpath)
        self.assertEqual(net_value_text.text, "kwota netto")
        self.close_advertisement()
        gross_value_number = self.get_driver().find_element_by_xpath(self.gross_value_number_xpath)
        self.assertEqual(gross_value_number.text, "7 797,62 PLN")
        gross_value_text = self.get_driver().find_element_by_xpath(self.gross_value_text_xpath)
        self.assertEqual(gross_value_text.text, "kwota brutto")

    def test_no_value_validation(self):
        """
        Test checks validation when there is no value set in 'Your salary'.
        """
        print("*** Test no value validation ***")
        evaluate = self.move_to_element(self.evaluate_button_id)
        evaluate.click()
        try:
            validation_error_elem = self.get_driver().find_element_by_xpath(self.validation_error_xpath)
        except NoSuchElementException as exception:
            print("Failed. No invalid value element.")
            raise exception
        self.assertEqual(validation_error_elem.text, "Podaj poprawną kwotę zarobków")

    def test_negative_value_validation(self):
        """
        Test checks validation if negative value is set to 'Your salary'.
        """
        print("*** Test negative value validation ***")
        value_text = self.get_driver().find_element_by_id(self.value_text_id)
        value_text.click()
        value_text.send_keys("-12345")
        evaluate = self.move_to_element(self.evaluate_button_id)
        evaluate.click()
        try:
            validation_error_elem = self.get_driver().find_element_by_xpath(self.validation_error_xpath)
        except NoSuchElementException as exception:
            print("Failed. No invalid value element.")
            raise exception
        self.assertEqual(validation_error_elem.text, "Podaj poprawną kwotę zarobków")

    def close_advertisement(self):
        """
        Switch of an advertisement.
        """
        try:
            advert_button = self.get_driver().find_element_by_xpath(self.advertisement_xpath)
            advert_button.click()
            print("An advertisement closed.")
        except ElementNotVisibleException:
            print("No advertisement.")

    def close_company_private_selection(self):
        """
        Switch of private section.
        """
        try:
            advert_button = self.get_driver().find_element_by_xpath(self.company_private_selection_class_name_xpath)
            advert_button.click()
            print("Company private closed.")
        except ElementNotVisibleException:
            print("No company privet.")

    def move_to_element(self, element_id):
        """
        Scroll down page and find element.
        """
        actions = ActionChains(self.get_driver())
        actions.move_to_element(self.get_driver().find_element_by_id(element_id)).perform()
        return self.get_driver().find_element_by_id(element_id)


class TestSalaryCalculatorChrome(TestSalaryCalculator):

    path_chrome_driver = r"C:\Python-geckodriver\chromedriver.exe"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(cls.path_chrome_driver)

    def get_driver(self):
        return self.driver


if __name__ == '__main__':
    unittest.main()
