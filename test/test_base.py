import unittest
from typing import Type, List, Any

from elements.base_form import BaseFormHandler
from pages.base_page import BasePage
from settings.settings import settings, browser_manager


class BaseTestCase(unittest.TestCase):
    """Класс содержит настройки для тестов."""
    page_class: Type[BasePage] = ...
    """класс страницы для инициализации в setUp"""

    browser_name: str = settings.DEFAULT_BROWSER
    """используемый браузер, по умолчанию Chrome"""

    options: list = settings.DEFAULT_BROWSER_OPTIONS
    """список опций для настройки браузера, необязательный параметр"""

    @classmethod
    def setUpClass(cls):
        """Инициализирует драйвер."""
        cls.driver = browser_manager.get_driver(cls.browser_name, cls.options)
        cls.settings = settings

    @classmethod
    def tearDownClass(cls):
        """Закрывает браузер после выполнения всех тестов"""
        cls.driver.close()

    def setUp(self):
        """Инициализирует страницу, устанавливает время ожидания для
        полной загрузки страницы"""

        self.page = self.page_class(self.driver, self.settings)

    def assertValueEqual(self,
                         value: Any,
                         expected_value: Any, msg: str = None) -> None:
        """Проверяет совпадают ли текущее значение с ожидаемым.

        :param value: текущее значение
        :param expected_value: ожидаемое значение
        :param msg: сообщение при несовпадении значений
        """

        self.assertEqual(value, expected_value, msg=msg)

    def assertFormInputs(self,
                         form: Type[BaseFormHandler],
                         inputs_list: List[str]) -> None:
        """Проверяет наличие и отображенние инпутов в форме из списка.

        :param form: объект формы, который содержит проверяемые инпуты
        :param inputs_list: список названий инпутов для проверки
        """

        for input_name in inputs_list:
            input_element = getattr(form, input_name)
            if not input_element.is_displayed():
                print(f'{input_name} данный инпут не найден в форме')
