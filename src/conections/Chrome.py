from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from src.conections.singleton import Singleton


class Chrome(metaclass=Singleton):

    def __init__(self):
        self.wait = None
        self.url = None
        service = Service(ChromeDriverManager().install())
        self.driver_chrome = webdriver.Chrome(service=service)
        self.driver_chrome.maximize_window()

    def set_url(self, url):
        self.url = url

    def set_connection(self):
        self.driver_chrome.get(self.url)
        self.wait = WebDriverWait(self.driver_chrome, 40)

    def close_browser(self):
        self.driver_chrome.close()
