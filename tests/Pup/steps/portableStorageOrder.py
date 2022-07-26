from behave import *

from tests.pages.CreateBlockOrderPage import CreateBlockOrderPage

use_step_matcher("re")


@step("I click on 'order portable storage' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    def go_to_Order_Portable_Storage_button(context):
        """
        :type context: behave.runner.Context
        """
        context.order_storage = CreateBlockOrderPage()
        context.order_storage.click_on_Portable_Storage_button()


@step('I fill Disk Description: "sq\] Portable created" text')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I fill Disk Description: "sq] Portable created" text')


@step('I Storage select Storage size : "10 GB \(SAN\)"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I Storage select Storage size : "10 GB (SAN)"')