from tests.pages.BasePage import BasePage


class FileBlockIndex(BasePage):
    """Clause represent to FileBlockIndex"""

    def __init__(self):
        """Constructor of class FileBlockIndex"""
        BasePage.__init__(self)

    def get_text_of_file_block_page(self, text):
        element = self.driver_chrome.find_element_by_xpath("// h3[contains(text(), 'Volumes')]").text
        assert element == text


