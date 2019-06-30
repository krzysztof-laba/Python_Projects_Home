from selenium import webdriver
import time


chrome_driver = r"C:\Python-geckodriver\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)


def open_page_on_new_tab():
    seconds = 1
    driver.maximize_window()
    # Open few pages on different tabs of web browser:
    driver.get("https://google.pl")
    time.sleep(seconds)
    driver.execute_script("window.open('http://twiter.com', 'new window 1')")
    time.sleep(seconds)
    driver.execute_script("window.open('https://bloodwars.interia.pl', 'new window 2')")
    time.sleep(seconds)
    driver.execute_script("window.open('https://en.wikipedia.org/wiki/Main_Page', 'new window 3')")
    time.sleep(seconds)
    driver.execute_script("window.open('http://twiter.com', 'new window 4')")

    # Switch between tabs on a web browser:
    # time.sleep(seconds)
    # driver.switch_to.window(driver.window_handles[0])
    # time.sleep(seconds)
    # driver.switch_to.window(driver.window_handles[-1])
    # time.sleep(seconds)
    # driver.switch_to.window(driver.window_handles[-2])

    # for i in driver.window_handles:
    #     time.sleep(seconds)
    #     driver.switch_to.window(i)
    #     print(i)

    for i in range(5):
        time.sleep(seconds)
        driver.switch_to.window(driver.window_handles[-i])
        print(-i)

    time.sleep(2)
    driver.close()


open_page_on_new_tab()
