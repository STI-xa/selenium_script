from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Settings:
    """Класс содержит настройки url и timeout"""
    BASE_URL = 'http://website:8000'
    """хост url"""

    URL_BRANCH_NAME = '/master/'
    """адрес ветки url"""

    SLEEP_TIME_SECONDS = 3
    """значение timeout в секундах"""

    DEFAULT_BROWSER = 'chrome'
    """браузер по умолчанию"""

    DEFAULT_BROWSER_OPTIONS = ['--start-maximized']
    """опции браузера, по умолчанию настроена опция разворачивания окна на
    весь экран"""


settings = Settings()


class BrowserManager:
    """Класс для выбора браузера и настройки его опций"""

    def get_driver(self,
                   browser_name: str,
                   options: List[str] = None) -> WebDriver:
        """
        Возвращает веб-драйвер для выбранного браузера.

        :param browser_name: название браузера, может быть 'chrome'
        или 'firefox'
        :param options: список опций для настройки браузера
        (необязательный параметр)
        :return: веб-драйвер для выбранного браузера
        """

        if browser_name == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            if options:
                for option in options:
                    chrome_options.add_argument(option)
            return webdriver.Chrome(options=chrome_options)
        elif browser_name == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            if options:
                for option in options:
                    firefox_options.add_argument(option)
            return webdriver.Firefox(options=firefox_options)
        else:
            raise ValueError(f'Браузер {browser_name} не поддерживается')


browser_manager = BrowserManager()
