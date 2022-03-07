import time

from behave import *

from src.conections.Chrome import Chrome


@given('I go to "{urlSrr}"')
def go_to_the_page(context, urlSrr):
    """
    :param urlSrr:
    :type context: behave.runner.Context
    """
    chrome_driver = Chrome(urlSrr)
    context.chrome = chrome_driver


@step('I select block protocol type')
def select_protocol_type(context):
    """
    :type context: behave.runner.Context
    """

    context.chrome.click_select_dropdown_srr()
    time.sleep(6)
    print("good")


@step('I enter cluster name with "{clusterName}", Management IP Address "{ipAddress}", Encryption key "{key}"')
def fill_form(context, clusterName, ipAddress, key):
    """
    :param clusterName:
    :type context: behave.runner.Context
    :type ipAddress: str
    :type key: str
    """
    context.chrome.srr_form_field(clusterName, ipAddress, key)


@step("I click on Preview SRR button")
def click_preview_page(context):
    """
    :type context: behave.runner.Context
    """
    context.chrome.click_create_srr()


@step("I click on Create SRR button")
def create_srr(context):
    """
    :type context: behave.runner.Context
    """
    context.chrome.click_finish_create()

