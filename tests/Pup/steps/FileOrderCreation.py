from behave import *
from tests.pages.CreateBlockOrderPage import CreateBlockOrderPage
from tests.pages.FileOrderPage import FileOrderPage

@step("I go to File list page")
def goto_File_List_page(context):
    """
    :type context: behave.runner.Context
    """
    context.file_storage = FileOrderPage()
    context.order_storage = CreateBlockOrderPage()
    context.file_storage.goto_File_storage_page()

@step("I click on Order_File_Storage button")
def click_order_file_Storage_button(context):
    """
    :type context: behave.runner.Context
    """
    context.file_storage = FileOrderPage()
    context.file_storage.click_on_Order_File_Storage()


@then("Successful modal shows")
def review_successfull_modal_shows(context):
    """
    :type context: behave.runner.Context
    """
    context.file_storage.verify_Success_Modal_shows()