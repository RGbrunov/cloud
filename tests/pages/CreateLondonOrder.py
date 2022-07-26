# import time
# from selenium.webdriver.common.by import By
# from tests.pages.BasePage import BasePage
# from selenium.webdriver.support import expected_conditions as EC
# from tests.pages.LoginPage import LoginPage
# from selenium.webdriver.support.select import Select
#
#
# class CreateLondonOrderClass(BasePage):
#     def __init__(self):
#         BasePage.__init__(self)
#
#     def goto_storage_page(self):
#         block_storage_Menu = self.driver_chrome.find_element(By.XPATH, "//span[normalize-space()='Block Storage']")
#         block_storage_Menu.click()
#
#     def click_on_e_region_option(self, e_region_name):
#         region_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Europe']")))
#         region_option.click()