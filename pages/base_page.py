from typing import Dict, List, Optional, Any
from urllib.parse import urlparse, parse_qs, urlencode

import requests
from selenium.webdriver.remote.webdriver import WebDriver

from settings.settings import settings


class BasePage:
    """Базовый класс предоставляет методы для работы с веб-страницей."""

    url: str = ...
    """url страницы, задается в классах-наследниках"""

    def __init__(self, driver: WebDriver, settings=settings) -> None:
        """
        Инициализирует объект веб-страницы.

        :param driver: Драйвер для взаимодействия с браузером
        :param settings: содержит настройки для работы скрипта
        """

        self.driver = driver
        """Драйвер для взаимодействия с браузером."""

        self.settings = settings
        """Содержит настройки для скрипта, такие как timeout, url"""

    def open(self, operation=None) -> 'BasePage':
        """Открывает веб-страницу."""
        full_url = (self.settings.BASE_URL + self.settings.URL_BRANCH_NAME +
                    self.url)
        if operation:
            params = {'operation': operation}
            full_url = f'{full_url}?{urlencode(params)}'
        response = requests.get(full_url)
        if response.status_code == 200:
            self.driver.get(full_url)
        else:
            raise Exception(f'Страница {full_url} недоступна, статус код: '
                            f'{response.status_code}')
        return self

    def refresh(self) -> 'BasePage':
        """Обновляет веб-страницу."""
        self.driver.refresh()
        return self

    def close(self) -> 'BasePage':
        """Закрывает веб-браузер."""
        self.driver.close()
        return self

    def get_url_params(self) -> Dict[str, List[str]]:
        """
        Извлекает и возвращает все параметры url текущей сессии.

        :return: словарь с параметрами url
        """

        parse_url = urlparse(self.driver.current_url)
        get_url_params = parse_qs(parse_url.query)
        return get_url_params

    def get_param(self,
                  param_name: str,
                  default_value: Optional[Any] = None) -> str:
        """Метод извлекает параметр из url в соответствии с полученным
        именем параметра.

        :param param_name: название параметра для извлечения
        :param default_value: значение, которое будет возвращено
        :return: строку с заданным параметром
        """

        url_params = self.get_url_params()
        get_param = url_params.get(param_name, [default_value])[0]

        print(f'{param_name}: {get_param}')
        return get_param
