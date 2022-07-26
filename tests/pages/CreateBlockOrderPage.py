import time
from selenium.webdriver.common.by import By
from tests.pages.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class CreateBlockOrderPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)

    def goto_storage_page(self):
        time.sleep(5)
        block_storage_Menu_link = self.driver_chrome.find_element(By.XPATH, "//span[normalize-space()='Block Storage']")
        block_storage_Menu_link.click()

    def click_on_Order_block_Storage(self):
        order_button = self.driver_chrome.find_element(By.CSS_SELECTOR, 'a[href="/cloud-storage/block/order"]')
        order_button.click()

    def click_on_region_option(self, region_name):
        region_option = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="id2"]')))
        region_option.click()

    def select_one_location(self, location_name):
        location_option = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div > div:nth-child(2) >fieldset >div> label.dl--tile-box__tile-0.bx--tile.bx--tile--selectable')))
        location_option.click()

    def select_and_click_in_zone(self, zone_name):
        time.sleep(5)
        zone_name_array = self.driver_chrome.find_elements(By.CSS_SELECTOR, 'label[class="dl--tile-box__tile-3 bx--tile bx--tile--selectable"]')
        zone_name_array[1].click()

    def select_one_billing_method(self, billing_m):
        billing_dropdown = self.driver_chrome.find_element(By.XPATH, '//*[@id="billing-method"]')
        select = Select(billing_dropdown)
        select.select_by_visible_text(billing_m)

    def fill_size_value(self, size):
        time.sleep(5)
        size_elem = self.driver_chrome.find_element(By.ID, "size-input")
        size_elem.clear()
        size_elem.send_keys(size)
        time.sleep(5)

    def select_one_snapshot_space(self, amount):
        snapshot_space = self.driver_chrome.find_element(By.ID, "snapshot-space")
        select = Select(snapshot_space)
        select.select_by_visible_text(amount)

    def select_one_OS_type(self, os_name):
        type_os_field = self.driver_chrome.find_element(By.CSS_SELECTOR, "#os-type")
        select = Select(type_os_field)
        select.select_by_visible_text(os_name)

    def select_endurance_iops(self, iops_value):
        endurance_iops = self.driver_chrome.find_element(By.CSS_SELECTOR, '#endurance__panel > fieldset > div > label:nth-child(6)')
        endurance_iops.click()

    def check_terms_and_condition(self):
        check_terms_con = self.driver_chrome.find_element(By.CSS_SELECTOR, 'span[class="bx--checkbox-label-text"]')
        check_terms_con.click()

    def press_on_create_button(self):
        create_button = self.driver_chrome.find_element(By.CSS_SELECTOR, 'button[class="bx--btn bx--btn--primary"]:nth-child(1)')
        create_button.click()