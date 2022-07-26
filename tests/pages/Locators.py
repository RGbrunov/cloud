from selenium.webdriver.common.by import By
from src.conections.Chrome import Chrome
import time
from selenium.webdriver.common.by import By

class mainPageLocators(object):
    FILESTORAGE_LINK = (By.XPATH, "//span[normalize-space()='File Storage']")
