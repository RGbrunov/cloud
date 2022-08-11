from src.conections.Chrome import Chrome


class BasePage:
    def __init__(self):
        chrome = Chrome()
        chrome.set_connection()
        self.driver_chrome = chrome.driver_chrome
        self.wait = chrome.wait
