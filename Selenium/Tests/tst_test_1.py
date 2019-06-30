from lerning.Selenium.Tests.mainPage import Main_page
from lerning.Selenium.Tests.mainPage import Home
import time



main_page = Main_page("Home")
main_page.navigate_to()
site_page = Home()
site_page.check_header()
site_page.check_text()
time.sleep(1)

main_page = Main_page("Basic HTML")
main_page.navigate_to()
time.sleep(1)

main_page = Main_page("Forms")
main_page.navigate_to()
time.sleep(1)

main_page = Main_page("Dynamic Content")
main_page.navigate_to()
time.sleep(1)

main_page = Main_page("CSS/XPath")
main_page.navigate_to()
time.sleep(1)

main_page.close_browser()