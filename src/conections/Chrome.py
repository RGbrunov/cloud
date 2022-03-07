from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Chrome:

    def __init__(self, url):
        """
        Constructor of the Chrome web driver.
        :param url:      string  email data.
        """
        service = Service(ChromeDriverManager().install())
        self.driver_chrome = webdriver.Chrome(service=service)
        self.driver_chrome.get(url)

    def click_login_button(self):
        """
        Clicks login button.
        """
        button = self.driver_chrome.find_element(By.CSS_SELECTOR, "a[href='/login']")
        button.click()

    def set_email_field(self, email):
        """
        Set email field.
        :param email:   string  email data.
        """
        email_field = self.driver_chrome.find_element(By.ID, "user")
        email_field.send_keys(email)

    """
        SRR def to specific locators
    """
    def srr_username_field(self, username):
        """
        Set username field.
        :param username:   string  email data.
        """
        username_field = self.driver_chrome.find_element(By.CSS_SELECTOR, "#user_username")
        username_field.send_keys(username)

    def click_login_button_srr(self):
        """
        Clicks login button.
        """
        button_login = self.driver_chrome.find_element(By.LINK_TEXT, "login")
        button_login.click()
        """
        Creating SRR
        """

    def click_select_dropdown_srr(self):
        """
        Clicks login button.
        """
        select_dropdown = self.driver_chrome.find_element(By.CSS_SELECTOR, "option#configureserviceresources_protocoltype_1")
        select_dropdown.click()

    def srr_form_field(self, clusterName, ipAddress, key):
        """
        Set username field.
        :param clusterName:
        """
        name_field = self.driver_chrome.find_element(By.ID, "configureserviceresources_datacenter")
        name_field.send_keys(clusterName)
        address_field = self.driver_chrome.find_element(By.ID, "configureserviceresources_managementipaddress")
        address_field.send_keys(ipAddress)
        key_field = self.driver_chrome.find_element(By.ID, "configureserviceresources_encryptionkey")
        key_field.send_keys(key)

    def click_create_srr(self):
        """
        Clicks login button.
        """
        click_button_srr = self.driver_chrome.find_element(By.ID, "fileblock_generateserviceresourcerecords_form_submit")
        click_button_srr.click()

    def click_finish_create(self):
        """
        Clicks login button.
        """
        click_button_finish_srr = self.driver_chrome.find_element(By.CSS_SELECTOR, "input.submitButton")
        click_button_finish_srr.click()

