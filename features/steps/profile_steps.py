import os
import time
from telnetlib import EC

from behave import given, when, then, use_step_matcher
from nose.tools import assert_equal
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import sys
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)
from main_functions import *
use_step_matcher("re")


@given(u'the user accesses the Fábrica de Sinais platform #3')
def accesses_platform3(context):
    context.browser = Firefox()
    context.browser.get("https://teste.leadfortaleza.com.br/fabricadesinais/#!/")
    login(context.browser, "jardesonusuario", "abcd1234")

@when(u'the user selects the Profile on the top menu')
def profile_menu(context):
    time.sleep(5)
    profile_menu = context.browser.find_element_by_link_text("Perfil")
    profile_menu.click()

@then(u'the platform returns to the user his profile information.')
def profile_information(context):
    time.sleep(3)
    profile_information = context.browser.find_element_by_xpath("/html/body/div/section/div/section/div[1]/div/div[1]/div/div[1]/h3").text
    assert_equal("Jardeson da Silva Santos", profile_information)
    context.browser.quit()