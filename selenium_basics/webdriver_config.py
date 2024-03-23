from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Locators:
    def __init__(self):
        self.service_object = Service(r"C:\Users\yasha\Desktop\selenium_drivers\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_object)
