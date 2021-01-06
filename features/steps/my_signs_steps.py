from telnetlib import EC

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from features.steps.utils.main_functions import login
from selenium.webdriver import Firefox

@given(u'the user accesses the Fábrica de Sinais platform #4')
def accesses_platform4(context):
    context.browser = Firefox()
    login(context.browser, "jardesonusuario", "abcd1234")

@when(u'the user selects the My Signals on the top menu')
def my_signs_menu(context):
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@ui-sref='mysigns']")))
    my_signs_menu = context.browser.find_element_by_xpath("//*[@ui-sref='mysigns']")
    my_signs_menu.click()

@then(u'the platform returns to the user the his suggested Signs')
def suggested_signs(context):
    suggested_signs = context.browser.find_element_by_css_selector("#signsFactoryMyDiscussions")
    suggested_signs.text()
    assert suggested_signs
    context.browser.quit()