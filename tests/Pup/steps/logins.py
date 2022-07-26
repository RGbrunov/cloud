import time
from behave import *
from tests.pages.LoginPage import LoginPage


@step('I go to the "{url}"')
def open_to_the_page(context, url):
    """
    Goes to a page according to 'url' parameter1
    :param url:   string    url page data.
    :type context: behave.runner.Context
    """
    context.connect_site = LoginPage()


@step('I fill the email field with "{email}"')
def set_user_mail_field(context, email):
    """
    Fills the email field according to 'email' parameter.
    :param email:   string    email data.
    :type context: behave.runner.Context
    """
    context.connect_site = LoginPage()
    context.connect_site.set_user_email_field(email)


@step('I click on continue button')
def press_continue_button(context):
    """
    Clicks on continue button
    :type context: behave.runner.Context
    """
    context.connect_site.press_continue_button()
    time.sleep(5)


@step('I enter "{password}" data')
def fill_password_field(context, password):
    """
    :param password:
    :type context: behave.runner.Context
    """
    context.connect_site.set_password_textfield(password)


@step("I press login button")
def click_login_button(context):
    """
    :type context: behave.runner.Context
    """
    context.connect_site.click_on_login_button()

@given("I click on navigation menu option")
def click_on_navigation_menu(context):
    """
    :type context: behave.runner.Context
    """
    context.connect_site.click_on_navigation_menu_option()

@given("I go to classic infrastructure")
def click_on_classic_infrastructure_link(context):
    """
    :type context: behave.runner.Context
    """
    context.connect_site.open_classic_infrastructure_link()


@step("I click on Storage link")
def click_on_storage_link(context):
    """
    :type context: behave.runner.Context
    """
    context.connect_site.open_storage_link()
    # wait = WebDriverWait(chrome_driver, 5)
    # wait.until(chrome_driver.open_storage_link())

@step("I hover mouse on classic Infrastructure")
def mouse_hover_classic_Infrastructure(context):
    """
    :type context: behave.runner.Context
    """
    context.connect_site.mouse_hover_on_menu()
