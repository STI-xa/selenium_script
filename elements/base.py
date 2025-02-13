from typing import Optional, Union

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings.settings import settings


class Base:
    """Базовый класс для управления элементами веб-страницы."""
    name: str = ...
    """Название элемента, задается в классах-наследниках"""

    locator: str = ...
    """Строка или список строк из xpath локатора(-ов) для поиска
    веб-элемента."""

    def __init__(self,
                 driver: WebDriver,
                 settings=settings,
                 parent: Optional[Union[str, int, list, dict]] = None,
                 name: Optional[str] = None) -> None:
        """
        :param driver: Драйвер для взаимодействия с браузером
        :param parent: Родительский элемент в контексте которого будет
        происходить поиск веб-элемента
        :param settings: Содержит настройки для скрипта, такие как timeout, url
        :param name: Название элемента для поиска, задается в
        классах-наследниках и передается в локатор
        """

        self.driver = driver
        """Драйвер для взаимодействия с браузером."""

        self.parent = parent
        """Родительский элемент в контексте которого будет происходить
        поиск веб-элемента."""

        self.settings = settings
        """Содержит настройки для скрипта, такие как timeout, url"""

        self.action = ActionChains(self.driver)
        """Метод позволяющий производить низкоуровневые операции: перемещение
        мыши, действия с кнопками/клавишами клавиатуры."""

        if name is not None:
        # Если значение 'name' передано, оно устанавливается как имя элемента
            self.name = name

        self._set_locator()  # Установка локатора для поиска элемента

    def _set_locator(self):
        """Метод, устанавливающий локатор для поиска элемента, требует
        реализации в дочерних классах."""

        raise NotImplementedError(f'Необходимо реализовать метод _set_locator '
                                  f'в {self.__class__.__name__} классе')

    def _validate_locator(self, locator=None) -> None:
        """
        Метод для валидации локатора, проверяет и выбрасывает исключение, если
        локатор пуст и если локатор начинается не с // или одной из осей xpath

        :param locator: используется дополнительный локатор для поиска
        элементов
        """
        xpath_exceptions = ['following', 'ancestor', 'sibling', 'parent',
                            'descendant']

        if locator is None:
            locator = self.locator

        if not locator:
            raise Exception('Локатор не может быть None')

        if not locator.startswith('//'):
            if not any(locator.startswith(axis + '::') for axis
                       in xpath_exceptions):
                raise ValueError(f'Локатор "{locator}" должен '
                                 f'начинаться с "//" или одной из осей: '
                                 f'{", ".join(xpath_exceptions)}')

    def find_element(self, timeout=None) -> WebElement:

        """
        Находит и возвращает веб-элемент на основе указанного локатора.
        Если указан родительский элемент, то поиск выполняется относительно
        него, иначе поиск будет выполняться в контексте драйвера.

        :param timeout: задает время ожидания элемента на странице
        """

        self._validate_locator()
        context = self.parent.find_element() if self.parent else self.driver
        timeout = timeout if timeout is not None \
            else self.settings.SLEEP_TIME_SECONDS
        try:
            element = WebDriverWait(
                context, timeout).until(EC.presence_of_element_located((
                    By.XPATH, self.locator)))
            return element
        except TimeoutException as e:
            raise TimeoutException(f'Элемент с локатором {self.locator} '
                                   f'не найден.') from e

    def find_multiple_elements(self,
                               locator: str = None,
                               timeout: int = None) -> list:

        """
        Находит и возвращает список веб-элементов на основе указанного
        локатора.
        Если указан родительский элемент, то поиск выполняется относительно
        него, иначе поиск будет выполняться в контексте драйвера.

        :param locator: используется дополнительный локатор для поиска
        элементов
        :param timeout: задает время ожидания элемента на странице
        """

        self._validate_locator()
        context = self.parent.find_element() if self.parent else self.driver
        timeout = timeout if timeout is not None \
            else self.settings.SLEEP_TIME_SECONDS
        locator = locator if locator is not None else self.locator
        try:
            elements = WebDriverWait(context, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, locator)))
            return elements
        except TimeoutException as e:
            raise TimeoutException(f'Элемент с локатором {locator} '
                                   f'не найден.') from e

    def is_displayed(self) -> bool:
        """Проверяет доступность элемента на веб-странице, если элемента нет
        на странице, перехватывает исключение."""

        try:
            element = self.find_element(timeout=0)
            if element.is_displayed():
                return True
        except TimeoutException:
            return False
