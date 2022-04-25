import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, i):
        self.i = i

    def wait_visibility_element_by_id(self, element_id, time=60):
        self.i.get()
        return WebDriverWait(self.i, time).until(EC.visibility_of_element_located((By.ID, element_id)))

    def get_all_links(self):
        elements = self.i.find_elements(By.XPATH, "//a[@href]")
        return [elem.get_attribute('href') for elem in elements]

    def get_status_code(self, url):
        return requests.get(url).status_code

    def remove_final_slash(self, url):
        if url[-1] == '/':
            url = url[:-1]
        return url
