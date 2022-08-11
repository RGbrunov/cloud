from tests.pages.BasePage import BasePage
from tests.pages.Locators import Locators


class LoginHome(BasePage):

    def __init__(self):

        BasePage.__init__(self)

    def srr_username_field(self, username):
        username_field = self.driver_chrome.find_element(*Locators.USERNAME)
        username_field.send_keys(username)

    def click_login_button(self):
        button_login = self.driver_chrome.find_element(*Locators.CLICK_ON_LOGIN)
        button_login.click()
