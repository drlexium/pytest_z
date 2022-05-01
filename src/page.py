import allure
import requests
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, i):
        self.i = i

    def get(self, url):
        """
        Окрывает страницу в браузере
        :param url: ссылка на страницу
        :return:
        """
        self.i.get(url)

    def get_current_url(self):
        """
        Возвращает текущий url стнаницы
        :return: текущий upl страницы
        """
        return self.i.current_url

    def wait_visibility_element_by_id(self, element_id, time=60):
        """
        Ожидаем, когда элемент с указанным ID станет видимым
        :param element_id: id элемента
        :param time: время ожидания
        :return:
        """
        # self.i.get()
        return WebDriverWait(self.i, time).until(ec.visibility_of_element_located((By.ID, element_id)))

    def get_all_links(self):
        """
        Получить все ссылки с текущей страницы
        :return: список ссылок
        """
        elements = self.i.find_elements(By.XPATH, "//a[@href]")
        assert elements is not None
        assert len(elements) > 0
        print("\nНайдено " + len(elements).__str__() + " ссылок.")
        return [elem.get_attribute('href') for elem in elements]

    @staticmethod
    def get_status_code(url):
        """
        Получить код статуса страницы по ссылке
        :param url: ссылка на страницу
        :return: код статуса
        """
        return requests.get(url).status_code

    @staticmethod
    def remove_final_slash(url):
        """
        Удаление слеша в конце строки если он там есть
        :param url: строка для обработки
        :return: строка - результат
        """
        if url[-1] == '/':
            url = url[:-1]
        return url

    def make_screenshot(self, filename):
        """
        Сделать скриншот
        :param filename: имя файла скриншота
        """
        allure.attach(self.i.get_screenshot_as_png(), name=filename, attachment_type=AttachmentType.PNG)

    def scroll_down(self):
        """
        Проскроллить страницу в самый низ
        """
        self.i.execute_script("window.scrollTo(0, document.body.scrollHeight);")
