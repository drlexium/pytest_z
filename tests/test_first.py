import allure
from selenium.webdriver.common.by import By
from src.page import Page


class TestFirstPy:

    @allure.feature('www.mos.ru')
    @allure.story('Анализ ссылок на https://www.mos.ru/')
    def test_see_page(self, i):
        with allure.step(f"Перейти на страницу https://www.mos.ru/"):
            i.get('https://www.mos.ru/')
            Page(i).make_screenshot('screen01')

        with allure.step(f"Проверить наличие шапки."):
            i.find_element(By.ID, "mos-header")
            assert True, i.is_element_visible(By.ID, "mos-header")
            Page(i).make_screenshot('screen02')

        with allure.step(f"Проверить наличие подвала."):
            i.find_element(By.ID, "mos_footer")
            Page(i).scroll_down()
            assert True, i.is_element_visible(By.ID, "mos_footer")
            Page(i).make_screenshot('screen03')

    def test_page_links(self, i):
        with allure.step(f"Вытащить все ссылки со страницы и проверить их на 200 (280 шт.)"):
            i.get('https://www.mos.ru/')
            links = Page(i).get_all_links()
            assert links is not None
            assert len(links) > 0
            print("\nНайдено " + len(links).__str__() + " ссылок.")
            for link in links:
                status = Page(i).get_status_code(link)
                if status == 200:
                    with allure.step(f"PASSED: Статус ссылки {link} равен 200"):
                        print(f"\033[32m PASSED: Статус ссылки {link} равен 200 \033[0m")
                else:
                    with allure.step(f"FAIL: Статус ссылки {link} равен {status}"):
                        print(f"\033[31m FAIL: Статус ссылки {link} равен {status} \033[0m")

        with allure.step(f"Открыть каждую ссылку и проверить адресную строку браузера, что открывается нужная ссылка"):
            for link in links:
                i.get(link)
                url = i.current_url

                # Избегаю ошибки, если url и link отличаются только "/" на конце
                link = Page(i).remove_final_slash(links)
                url = Page(i).remove_final_slash(url)

                # Проверяю соответствие адреса страницы ссылке на страницу
                if link == url:
                    with allure.step(f"PASSED: Адрес страницы \"{url}\" совпадает со ссылкой: \"{link}\""):
                        print(f"\033[32m PASSED: Адрес страницы \"{url}\" совпадает со ссылкой: \"{link}\" \033[0m")
                else:
                    with allure.step(f"FAIL: Адрес страницы \"{url}\" НЕ совпадает со ссылкой: \"{link}\""):
                        print(f"\033[31m FAIL: Адрес страницы \"{url}\" НЕ совпадает со ссылкой: \"{link}\" \033[0m")
