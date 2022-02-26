from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Chrome:

    def __init__(self, url):
        service = Service(ChromeDriverManager().install())
        self.driver_chrome = webdriver.Chrome(service=service)
        self.driver_chrome.get(url)

    def click_button(self):
        button = self.driver_chrome.find_element(By.CSS_SELECTOR, "a[href='/login']")
        button.click()

    def set_email_field(self, email):
        email_field = self.driver_chrome.find_element(By.ID, "user")
        email_field.send_keys(email)
