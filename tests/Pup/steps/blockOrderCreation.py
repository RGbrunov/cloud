from tests.pages.CreateBlockOrderPage import CreateBlockOrderPage
from behave import *


@given("I go to block list page")
def go_block_storage_page(context):
    """
    :type context: behave.runner.Context
    """
    context.order_storage = CreateBlockOrderPage()
    context.order_storage.goto_storage_page()


@step("I click on Order_Block_Storage button")
def click_on_Order_Block_Storage_button(context):
    """
    :type context: behave.runner.Context
    """
    context.order_storage = CreateBlockOrderPage()
    context.order_storage.click_on_Order_block_Storage()


@step('I click on "{region_name}" region')
def select_and_click_region(context, region_name):
    """
    :param region_name:
    :type context: behave.runner.Context
    """
    context.order_storage.click_on_region_option(region_name)


@step('I select "{location_name}" location')
def select_and_click_on_location(context, location_name):
    """
    :param location_name:
    :type context: behave.runner.Context
    """
    context.order_storage.select_one_location(location_name)

@step('I click on "{zone_name}" zone')
def select_and_click_on_zone(context, zone_name):
    """
    :param zone_name:
    :type context: behave.runner.Context
    """
    context.order_storage.select_and_click_in_zone(zone_name)

@step('I select "{billing_m}"  billing method')
def select_billing_method(context, billing_m):
    """
    :param billing_m:
    :type context: behave.runner.Context
    """
    context.order_storage.select_one_billing_method(billing_m)


@step('I fill the order size "{size}"')
def fill_size_storage_value(context, size):
    """
    :param size:
    :type context: behave.runner.Context
    """
    context.order_storage.fill_size_value(size)

@step('I select snapshot space "{amount}"')
def select_snapshot_space(context, amount):
    """
    :param amount:
    :type context: behave.runner.Context
    """
    context.order_storage.select_one_snapshot_space(amount)

@step('I select "{os_name}" OS type')
def select_one_OS(context, os_name):
    """
    :type context: behave.runner.Context
    """
    context.order_storage.select_one_OS_type(os_name)

@step('I Select "{iops_value}" IOPS option')
def select_one_iops_option(context, iops_value):
    """
    :param iops_value:
    :type context: behave.runner.Context
    """
    context.order_storage.select_endurance_iops(iops_value)

@step("I checked I have read and agree to the terms and conditions checkbox")
def checked_terms_and_conditions(context):
    """
    :type context: behave.runner.Context
    """
    context.order_storage.check_terms_and_condition()

@step("I click on create button")
def click_on_create_button(context):
    """
    :type context: behave.runner.Context
    """
    context.order_storage.press_on_create_button()