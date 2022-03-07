from behave import *

from src.conections.Chrome import Chrome


@step('I go to the "{url}"')
def open_to_the_page_srr(context, url):
    """
    :param url:
    :type context: behave.runner.Context
    """
    chrome_driver = Chrome(url)
    context.chrome = chrome_driver


@step('I enter Username with "{username}"')
def enter_username(context, username):
    """
    :param username:
    :type context: behave.runner.Context
    """
    context.chrome.srr_username_field(username)


@step("I click on login button")
def click_on_login_button_srr(context):
    """
    :type context: behave.runner.Context
    """
    context.chrome.click_login_button_srr()


@then("User must successfully login")
def login_message(context):
    """
    :type context: behave.runner.Context
    """
    print("Successfully login")
