from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login(browser, username, password):

    browser.get("https://teste.leadfortaleza.com.br/fabricadesinais/#!/")
    login_button = browser.find_element_by_css_selector("button[class='btn-login']")
    login_button.click()

    login_field = browser.find_element_by_css_selector("input[id='login']")
    login_field.send_keys(username)
    password_field = browser.find_element_by_css_selector("input[id='password']")
    password_field.send_keys(password)
    button_enter = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button_enter.click()