from selenium.webdriver.common.by import By


class Locators(object):
    """Clause represent to Locators"""

    # LoginHome
    USERNAME = (By.CSS_SELECTOR, "#user_username")
    CLICK_ON_LOGIN = (By.LINK_TEXT, "login")


