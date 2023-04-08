# 7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
# http://suninjuly.github.io/xpath_examples

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
xpath_testing = ["//button[text()='Gold']", "/html/body/div[2]/button[3]", "//div[2]/button[@class='btn'][3]"]
css_testing = ["body > div:nth-child(2) > button:nth-child(3)", "body div:nth-child(2) button:nth-last-child(2)",
               ".bg-light div:nth-of-type(2) button.btn:nth-of-type(3)", ".bg-light div:nth-of-type(2) button.btn:nth-last-of-type(2)"]


def open_page():
    browser.get('http://suninjuly.github.io/xpath_examples')


def find_element(by, lst):
    for i in lst:
        cat = browser.find_element(by, i)
        print(f'{by}: "{i}", "{cat.text}", {cat}')


def test_open_page():
    open_page()


def test_find_element_xpath():
    find_element(By.XPATH, xpath_testing)


def test_find_element_css_selector():
    find_element(By.CSS_SELECTOR, css_testing)
