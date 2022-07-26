import time
from selenium.webdriver.common.by import By
from tests.pages.BasePage import BasePage

class FileOrderPageTest(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def region_label_exists(self):
        region_label = self.driver_chrome.find_element(By.XPATH, "legend[contains(text(),'Region')]")
        region_label.isDisplayed()
