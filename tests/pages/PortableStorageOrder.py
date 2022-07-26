import time
from selenium.webdriver.common.by import By
from tests.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class PortableStorageOrder(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def click_on_Portable_Storage_button(self):
        order_button = self.driver_chrome.find_element(By.CSS_SELECTOR, 'a[href="/cloud-storage/portable/order"]')
        order_button.click()


