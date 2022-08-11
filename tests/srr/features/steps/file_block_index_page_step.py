from behave import *

from tests.pages.FileBlockIndex import FileBlockIndex


@then('I need to see the text with "{text}" on FileBlock page')
def get_text(context, text):
    context.index_FB = FileBlockIndex()
    context.index_FB.get_text_of_file_block_page(text)
