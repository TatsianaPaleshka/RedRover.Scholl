import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
my_email = ''
my_password = ''
inbox_email = ''
change_my_password_link = ''


def open_page():
    browser.get('https://home.openweathermap.org/users/sign_in')


def test_open_page():
    open_page()
    assert 'openweathermap' in browser.current_url


def test_find_element_lost_password():
    lost_password_text = browser.find_element(By.CSS_SELECTOR, '.pwd-lost-q.show')
    assert 'Lost your password?' in lost_password_text.text
    lost_password_link = browser.find_element(By.CSS_SELECTOR, '.pwd-lost-q.show a')
    assert 'Click here to recover.' in lost_password_link.text
    lost_password_link.click()
    time.sleep(5)


def test_find_element_enter_email():
    enter_email_text = browser.find_element(By.CSS_SELECTOR, '.text-muted')
    assert 'Enter your email address and we will send you a link to reset your password.' in enter_email_text.text
    enter_email_field = browser.find_element(By.CSS_SELECTOR, '.pwd-lost .form-control.string.email.optional')
    assert 'Enter email' in enter_email_field.get_attribute('placeholder')
    enter_email_field.send_keys(my_email)


def test_check_send_email():
    send_button = browser.find_element(By.CSS_SELECTOR, ".pwd-lost-f.show.animated.fadeIn input[value='Send']")
    send_button.click()
    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                            '.col-md-6.col-md-offset-3.col-sm-8.col-sm-offset-2 div.panel.panel-green div.panel-body'),
                            'You will receive an email with instructions on how to reset your password in a few minutes.'))


def test_check_open_inbox_email():
    browser.get(inbox_email)
    


def test_check_change_password():
    browser.get(change_my_password_link)
    enter_password_field = browser.find_element(By.CSS_SELECTOR,
                                                '.form-group.password.optional.user_password #user_password')
    assert 'Password' in enter_password_field.get_attribute('placeholder')
    enter_password_field.send_keys(my_password)
    enter_repeat_password_field = browser.find_element(By.CSS_SELECTOR,
                            '.form-group.password.optional.user_password_confirmation #user_password_confirmation')
    assert 'Repeat Password' in enter_repeat_password_field.get_attribute('placeholder')
    enter_repeat_password_field.send_keys(my_password)
    change_my_password_button = browser.find_element(By.CSS_SELECTOR, "input[value='Change my password']")
    change_my_password_button.click()
    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                            '.col-md-6.col-md-offset-3.col-sm-8.col-sm-offset-2 div.panel.panel-green div.panel-body'),
                            'Your password has been changed successfully.'))


def test_check_after_change_password():
    browser.get('https://home.openweathermap.org/users/sign_in')
    enter_email_field = browser.find_element(By.CSS_SELECTOR, '.input-group #user_email')
    assert 'Enter email' in enter_email_field.get_attribute('placeholder')
    enter_email_field.send_keys(my_email)
    enter_password_field = browser.find_element(By.CSS_SELECTOR, '.input-group #user_password')
    assert 'Password' in enter_password_field.get_attribute('placeholder')
    enter_password_field.send_keys(my_password)
    submit_button = browser.find_element(By.CSS_SELECTOR, "#new_user input[value='Submit']")
    submit_button.click()
    WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                            '.col-md-6.col-md-offset-3.col-sm-8.col-sm-offset-2 div.panel.panel-green div.panel-body'),
                            'Signed in successfully.'))
