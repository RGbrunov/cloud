from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from src.conections.singleton import Singleton


class Chrome(metaclass=Singleton):

    def __init__(self):
        """
        Constructor of the Chrome web driver.
        :param url:      string  email data.
        """

        service = Service(ChromeDriverManager().install())
        self.driver_chrome = webdriver.Chrome(service=service)
        self.driver_chrome.maximize_window()
        self.driver_chrome.get("https://dev.console.test.cloud.ibm.com")
        self.action = ActionChains(self.driver_chrome)
        self.wait = WebDriverWait(self.driver_chrome, 40)
