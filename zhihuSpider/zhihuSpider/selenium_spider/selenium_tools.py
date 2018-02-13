
from selenium import webdriver

def get_cookies():
    browser = webdriver.Chrome()

    browser.get("https://www.zhihu.com/signin")
    browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys(
        "18782902568")
    browser.find_element_by_css_selector(".SignFlow-password input").send_keys(
        "admin321")
    browser.find_element_by_css_selector(
        ".Button.SignFlow-submitButton").click()
    import time
    time.sleep(10)
    Cookies = browser.get_cookies()

    return Cookies