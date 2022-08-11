from behave import fixture

from src.conections.Chrome import Chrome


@fixture
def before_all(context):
    url = context.config.userdata['url']
    chrome = Chrome()
    chrome.set_url(url)


# before every scenario
def before_scenario(scenario, context):
    print('Before scenario executed')


# after every feature
def after_feature(scenario, context):
    print('After feature executed')


# after all
def after_all(context):
    chrome = Chrome()
    chrome.close_browser()
    print('After all executed')
