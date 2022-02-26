from behave import *

from src.conections.Chrome import Chrome


@step('I go to the "{url}"')
def open_to_the_page(context, url):
    """
    Goes to a page according to 'url' parameter1
    :param url:   string    url page data.
    :type context: behave.runner.Context
    """
    chrome_driver = Chrome(url)
    context.chrome = chrome_driver


@step("I click on login button")
def click_on_login_button(context):
    """
    Clicks on login button
    :type context: behave.runner.Context
    """
    chrome_driver = context.chrome
    chrome_driver.click_login_button()


@step('I fill the email field with "{email}"')
def step_impl(context, email):
    """
    Fills the email field according to 'email' parameter.
    :param email:   string    email data.
    :type context: behave.runner.Context
    """
    context.chrome.set_email_field(email)
