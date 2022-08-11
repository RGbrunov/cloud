from behave import *

from tests.pages.LoginHome import LoginHome


@step('I go to the url')
def open_to_the_page_srr(context):
    context.login_home = LoginHome()


@step('I enter Username')
def enter_username(context):
    context.login_home = LoginHome()
    username = context.config.userdata['username']
    context.login_home.srr_username_field(username)


@step("I click on Login button")
def click_on_login_button(context):
    context.login_home.click_login_button()





