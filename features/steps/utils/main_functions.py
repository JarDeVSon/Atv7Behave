import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login(browser, username, password):

    time.sleep(20)
    #wait = WebDriverWait(browser, 20)
    #wait.until(EC.element_to_be_clickable((By.ID, "btLogin")))

    login_button = browser.find_element_by_id("btLogin")
    login_button.click()


    login_field = browser.find_element_by_id("login")
    login_field.send_keys(username)
    password_field = browser.find_element_by_id("password")
    password_field.send_keys(password)
    button_enter = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button_enter.click()