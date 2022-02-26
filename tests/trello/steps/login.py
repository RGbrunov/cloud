from behave import *

from src.conections.Chrome import Chrome


@step('I go to the "{url}"')
def i_go_to_the_page(context, url):
    """
    :param url:
    :type context: behave.runner.Context
    """
    chrome_driver = Chrome(url)
    context.chrome = chrome_driver


@step("I click on login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    chrome_driver = context.chrome
    chrome_driver.click_button()


@step('I fill the email field with "{email}"')
def step_impl(context, email):
    """
    :param email:
    :type context: behave.runner.Context
    """
    context.chrome.set_email_field(email)
