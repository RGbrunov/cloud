from selenium.webdriver.support.wait import WebDriverWait

from src.conections.Chrome import Chrome

class BasePage:
    def __init__(self):
        self.chrome = Chrome()
        self.driver_chrome = self.chrome.driver_chrome
        self.action = self.chrome.action
        self.wait = self.chrome.wait
