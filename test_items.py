from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

"""
pytest -s -v --browser_name=firefox test_cmd.py
"""
#print(language)
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def check_if_add_to_cart_button_visible(browser):
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").is_displayed()
    except:
        return False
    else:
        return True

def test_presence_button_add_to_cart(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    #time.sleep(30)
    is_button_add_to_cart_visible = check_if_add_to_cart_button_visible(browser)
    assert is_button_add_to_cart_visible == True, "Кнопка добавления товара в корзину отсутствует на странице!"