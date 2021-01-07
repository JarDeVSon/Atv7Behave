import os
import time
from telnetlib import EC
from behave import when, then, given, use_step_matcher
from nose.tools import assert_equal
from selenium.webdriver import Firefox
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)
from main_functions import *
use_step_matcher("re")

@given(u'the user accesses the Fábrica de Sinais platform #2')
def accesses_platform2(context):
    context.browser = Firefox()
    context.browser.get("https://teste.leadfortaleza.com.br/fabricadesinais/#!/")
    login(context.browser, "jardesonusuario", "abcd1234")

@when(u'the user selects the Glossary on the top menu')
def glossary_menu(context):
    time.sleep(5)
    #wait = WebDriverWait(context.browser, 20)
    #wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Glossário")))
    glossary_menu = context.browser.find_element_by_link_text("Glossário")
    glossary_menu.click()

@then(u'the platform returns to the user the glossary items in alphabetical order')
def glossary_items(context):
    glossary_items = context.browser.find_element_by_xpath("/html/body/div[1]/section/div/section/div[1]/div[1]/h4").text
    assert_equal("Itens do Glossário", glossary_items)
    context.browser.quit()
