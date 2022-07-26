import time
from selenium.webdriver.common.by import By

from tests.pages import Locators
from tests.pages.BasePage import BasePage
from tests.pages.Locators import mainPageLocators


class FileOrderPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def goto_File_storage_page(self):
        time.sleep(5)
        File_storage_Menu_link = self.driver_chrome.find_element(*mainPageLocators.FILESTORAGE_LINK)
        File_storage_Menu_link.click()

    def click_on_Order_File_Storage(self):
        order_button = self.driver_chrome.find_element(By.CSS_SELECTOR, 'a[href="/cloud-storage/file/order"]')
        order_button.click()

    def verify_Success_Modal_shows(self):
        modal_window = self.driver_chrome.find_element(By.CSS_SELECTOR, 'h3[class="bx--modal-header__heading"]:nth-child(1)')
        modal_window.isDisplayed()

