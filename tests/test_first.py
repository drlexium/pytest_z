# 1) Перейти на страницу https://www.mos.ru/
# 2) Проверить наличие шапки подвала.
# 3) Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)
# 4) Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from src.page import Page


class TestFirstPy:

    # 1) Перейти на страницу https://www.mos.ru/
    def test_see_page(self, i):
        """Перейти на страницу https://www.mos.ru/"""
        i.get('https://www.mos.ru/')

    # 2) Проверить наличие шапки.
    def test_see_header(self, i):
        """Проверить наличие шапки."""
        i.find_element(By.ID, "mos-header")

    # 2) Проверить наличие подвала.
    def test_see_footer(self, i):
        """Проверить наличие подвала."""
        i.find_element(By.ID, "mos_footer")

    # 3) Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)
    def test_links_codes(self, i):
        """Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)"""
        links = Page(i).get_all_links()
        assert links is not None
        assert len(links) > 0
        print("\nНайдено " + len(links).__str__() + " ссылок.")
        for link in links:
            status = Page(i).get_status_code(link)
            if status == 200:
                print(f"\033[32m Статус ссылки {link} равен 200 \033[0m")
            else:
                print(f"\033[31m Статус ссылки {link} равен {status} \033[0m")

    # 4) Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка
    def test_links_redirect(self, i):
        """Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка"""
        links = Page(i).get_all_links()
        assert links is not None
        assert len(links) > 0
        print("\nНайдено " + len(links).__str__() + " ссылок.")
        for link in links:
            # Перехожу по ссылке
            i.get(link)
            # Получаю адрес страницы
            url = i.current_url

            # Избегаю ошибки, если url и link отличаются только "/" на конце
            link = Page(i).remove_final_slash(links)
            url = Page(i).remove_final_slash(url)

            # Проверяю соответствие адреса страницы ссылке на страницу
            if link == url:
                print("\033[32m Ссылка на страницу " + url + " совпадает со ссылкой в тэге: " + link + "\033[0m")
            else:
                print("\033[31m Ссылка на страницу " + url + " НЕ совпадает со ссылкой в тэге: " + link + "\033[0m")
