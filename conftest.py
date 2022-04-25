import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='class')
def i():
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"c:\selenium_browsers\download",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}

    driver = webdriver.Chrome(executable_path=r"C:\selenium_browsers\chromedriver.exe",
                              desired_capabilities=capabilities,
                              chrome_options=options)
    driver.maximize_window()
    print('Стартую пачку тестов')
    yield driver
    print('Тесты пройдены')
    driver.close()
    driver.quit()



