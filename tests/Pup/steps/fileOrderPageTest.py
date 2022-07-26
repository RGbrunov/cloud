from behave import *
from tests.pages.FileOrderPageTest import FileOrderPageTest
from tests.pages.LoginPage import LoginPage

@step("I go to region section")
def review_region_shows(context):
    """
    :type context: behave.runner.Context
    """
    context.file_order_page = FileOrderPageTest()
    # context.connect_site = LoginPage()
    context.file_order_page.region_label_exists()