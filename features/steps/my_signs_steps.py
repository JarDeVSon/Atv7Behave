import os
from telnetlib import EC

from behave import given, when, then, use_step_matcher
from nose.tools import assert_equal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import Firefox
import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)
from main_functions import *
use_step_matcher("re")

@given(u'the user accesses the Fábrica de Sinais platform #4')
def accesses_platform4(context):
    context.browser = Firefox()
    context.browser.get("https://teste.leadfortaleza.com.br/fabricadesinais/#!/")
    login(context.browser, "jardesonusuario", "abcd1234")

@when(u'the user selects the My Signals on the top menu')
def my_signs_menu(context):
    my_signs_menu = context.browser.find_element_by_link_text("Meus Sinais")
    my_signs_menu.click()

@then(u'the platform returns to the user the his suggested Signs')
def suggested_signs(context):
    suggested_signs = context.browser.find_element_by_id("signsFactoryMyDiscussions")
    assert_equal("Meus sinais sugeridos", suggested_signs)
    context.browser.quit()