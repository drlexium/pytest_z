import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, i):
        self.i = i

    def wait_element_by_id(self, element_id, time=60):
        wait = WebDriverWait(self.i, time)
        return wait.until(EC.visibility_of_element_located((By.ID, element_id)))
