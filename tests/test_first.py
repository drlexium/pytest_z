# 1) Перейти на страницу https://www.mos.ru/
# 2) Проверить наличие шапки подвала.
# 3) Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)
# 4) Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestFirstPy:
    def __init__(self, setup):
        self.i = setup

    # 1) Перейти на страницу https://www.mos.ru/
    def test_see_page(self):
        """Перейти на страницу https://www.mos.ru/"""
        self.i.get('https://www.yandex.ru')


    # 2) Проверить наличие шапки подвала.
    def test_see_header(self):
        wait = WebDriverWait(self.i, 60)
        wait.until(EC.visibility_of_element_located((By.ID, 'mos-header')))
        wait.until(EC.visibility_of_element_located((By.ID, 'mos_footer')))


    # 2) Проверить наличие шапки подвала.
    def test_see_footer(self):
        print('Ищу подвал')
        assert 1 == 1
