
from behave import when, then, given
from selenium.webdriver import Firefox

from features.steps.utils.main_functions import login


@given(u'the user accesses the Fábrica de Sinais platform #2')
def accesses_platform2(context):
    context.browser = Firefox()
    login(context.browser, "jardesonusuario", "abcd1234")

@when(u'the user selects the Glossary on the top menu')
def glossary_menu(context):
    glossary_menu = context.browser.find_element_by_link_text("Glossário")
    glossary_menu.click()

@then(u'the platform returns to the user the glossary items in alphabetical order')
def glossary_items(context):
    glossary_items = context.browser.find_element_by_class_name("pagination-alphabetic")
    assert glossary_items
    context.browser.quit()
