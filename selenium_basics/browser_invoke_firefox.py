import time

from selenium import webdriver
# from webdriver.chrome import ChromeDriverManager

#Chrome driver Service
class BrowserInvoke:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def browser(self):
        driver = self.driver
        driver.get()
        time.sleep(4)
#         maximize screen
        driver.maximize_window()
#         to know/grab title
        print(driver.title)
#         to know url
        print(driver.current_url)


invoke = BrowserInvoke()
invoke.browser()
