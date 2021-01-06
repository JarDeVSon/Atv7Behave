

def login(browser, username, password):

    browser.implicitly_wait(5)
    login_button = browser.find_element_by_id("btLogin")
    login_button.click()


    login_field = browser.find_element_by_id("login")
    login_field.send_keys(username)
    password_field = browser.find_element_by_id("password")
    password_field.send_keys(password)
    button_enter = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button_enter.click()