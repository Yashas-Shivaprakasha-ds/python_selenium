import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class locators():
    def __init__(self):
        self.service_object = Service(r"C:\Users\yasha\Desktop\selenium_drivers\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_object)

    def identifying_locators(self):
        driver = self.driver
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        # identify elements by ID, Xpath, CSSSelector, Classname, name, linkText
        # prefer id as it wil be unique
        driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        # Click on checkbox
        driver.find_element(By.ID, "exampleCheck1").click()

        # handle xpath
        # //tagname[@attribute="value"]--> //input[@type="submit"] ---->xpath
        driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # .text is used to grab the from the class given
        message_confirmation = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message_confirmation)

        # handle CSS
        # tagname[attribute = "value"]--> input[type = "submit"] ---->css
        driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("shiva")

        assert "Success! The Form has been submitted successfully!.1234" in message_confirmation
        time.sleep(5)


locators_class = locators()
locators_class.identifying_locators()