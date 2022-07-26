import time
from selenium.webdriver.common.by import By
from tests.pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def click_login_button(self):
        """
       Clicks login button.
       """
        button = self.driver_chrome.find_element(By.CSS_SELECTOR, "a[href='/login']")
        button.click()

    def set_user_email_field(self, email):
        """
        Set email field.
        :param self:
        :param email:   string  email data.
        """
        time.sleep(5)
        email_field = self.driver_chrome.find_element(By.ID, "userid")
        email_field.send_keys(email)
        time.sleep(5)

    def press_continue_button(self):
        """
        Clicks continue button.
        """
        continue_button = self.driver_chrome.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[3]/button[1]/div[1]")
        time.sleep(2)
        continue_button.click()

    def set_password_textfield(self, password):
        """
        Fill password textfield
        :return:
        """
        time.sleep(2)
        password_field = self.driver_chrome.find_element(By.ID, "password")
        password_field.send_keys(password)

    def click_on_login_button(self):
        time.sleep(2)
        login_button = self.driver_chrome.find_element(By.XPATH, "//div[2]/button")
        login_button.click()

    def click_on_navigation_menu_option(self):
        time.sleep(7)
        # menu  navigation  icon
        navigation_menu = self.driver_chrome.find_element(By.XPATH, '//*[@id="global-header"]/header/div[1]/div[1]/div/button')
        navigation_menu.click()

    def open_classic_infrastructure_link(self):
        time.sleep(10)
        classic_infrastructure_link = self.driver_chrome.find_element(By.XPATH, "//*[@id='gen1-menu']/span/span[1]")
        classic_infrastructure_link.click()
        time.sleep(8)

    def mouse_hover_on_menu(self):
        classic_menu = self.driver_chrome.find_element(By.XPATH, "//*[@id='gen1-menu']/span/span[1]")
        self.action.move_to_element(classic_menu).perform()
        # time.sleep(5)
        # block_storage_Menu_link = self.driver_chrome.find_element(By.XPATH, "//span[normalize-space()='Block Storage']")
        # block_storage_Menu_link.click()

