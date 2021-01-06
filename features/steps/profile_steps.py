from telnetlib import EC

from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from features.steps.utils.main_functions import login


@given(u'the user accesses the Fábrica de Sinais platform #3')
def accesses_platform3(context):
    context.browser = Firefox()
    login(context.browser, "jardesonusuario", "abcd1234")

@when(u'the user selects the Profile on the top menu')
def profile_menu(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@ui-sref='profile']")))
    profile_menu = context.browser.find_element_by_xpath("//*[@ui-sref='profile']")
    profile_menu.click()

@then(u'the platform returns to the user his profile information.')
def profile_information(context):
    context.browser = Firefox()
    profile_information = context.browser.find_element_by_class_name("col-xs-12 text-center")
    profile_information.text()
    assert profile_information
    context.browser.quit()