import time
from selenium.webdriver.common.by import By


def test_basket_button(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(button) > 0, "Кнопка Добавить в корзину не найдена"

