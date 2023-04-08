# 7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете
# подобрать, тем лучше
# http://suninjuly.github.io/cats.html

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
xpath_testing = ["//*[contains(text(),'Fully charged cat')]", "//*[text()='Fully charged cat']",
                 "//p[text()='Fully charged cat']", "/html/body/main/div/div/div/div[5]/div/div/p"]
css_testing = ["body > main > div > div > div > div:nth-child(5) > div > div > p", "body :nth-child(5) div div p",
               "body .row :nth-of-type(5) div.card-body p", ".row :nth-child(5) p"]


def open_page():
    browser.get('http://suninjuly.github.io/cats.html')


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
