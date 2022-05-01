import allure
import requests
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.page import Page


class Mos:
    def __init__(self, i):
        self.i = i

    def see_header(self):
        """
        Проверить видимость шапки сайта
        """
        self.i.find_element(By.ID, "mos-header")
        assert True, self.i.is_element_visible(By.ID, "mos-header")

    def see_footer(self):
        """
        Проверить видимость подвала сайта
        """
        self.i.find_element(By.ID, "mos_footer")
        Page(self.i).scroll_down()
        assert True, self.i.is_element_visible(By.ID, "mos_footer")
