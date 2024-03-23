import time

from webdriver_config import  Locators

locator_instance = Locators()

def xpath_css_selectors():
    locator_instance.driver.get("https://rahulshettyacademy.com/angularpractice/")
    locator_instance.driver.maximize_window()
    # Click on radio button
    time.sleep(5)

xpath_css_selectors()