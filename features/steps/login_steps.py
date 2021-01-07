from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Firefox
from behave import given, when, then
from nose.tools import assert_equal
from selenium.webdriver.support.wait import WebDriverWait


@given(u'the user accesses the Fábrica de Sinais platform')
def accesses_platform(context):
    context.browser = Firefox()
    context.browser.get("https://teste.leadfortaleza.com.br/fabricadesinais/#!/")

    wait = WebDriverWait(context.browser, 20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn-login']")))
    login_button = context.browser.find_element_by_css_selector("button[class='btn-login']")
    login_button.click()

@when(u'the user authenticates with valid credentials')
def authenticates(context):
    wait = WebDriverWait(context.browser, 20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='login']")))
    login_field = context.browser.find_element_by_css_selector("input[id='login']")
    login_field.send_keys("jardesonusuario")
    password_field = context.browser.find_element_by_css_selector("input[id='password']")
    password_field.send_keys("abcd1234")
    button_enter = context.browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button_enter.click()

@then(u'the platform returns a welcome message to the user.')
def welcome_message(context):
    welcome_message = context.browser.find_element_by_xpath("//h3[@class='ng-binding']").text
    assert_equal("Olá, jardesonusuario!", welcome_message)
    context.browser.quit()
