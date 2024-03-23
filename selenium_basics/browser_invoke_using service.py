import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver.chrome import ChromeDriverManager

#Chrome driver Service
class BrowserInvoke:
    def __init__(self):
        driver_path = "C:\\Users\\yasha\\Desktop\\selenium_drivers\\chromedriver-win64\\chromedriver.exe"
        self.driver = driver_path

    def browser(self):
        driver = self.driver
        driver.get("https://rahulsheetyacademy.com")
        time.sleep(4)
#         maximize screen
        driver.maximize_window()
#         to know/grab title
        print(driver.title)
#         to know url
        print(driver.current_url)


invoke = BrowserInvoke()
invoke.browser()
