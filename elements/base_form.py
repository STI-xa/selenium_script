from selenium.webdriver.remote.webelement import WebElement

from elements.base import Base


class BaseFormHandler(Base):
    """Базовый класс предоставляет методы для взаимодействия с формой."""

    name: str = ...
    """Название формы, задается в классах-наследниках"""

    def _set_locator(self) -> 'BaseFormHandler':
        """
        Метод устанавливает локатор для поиска формы.

        :return self: возвращает текущий экземпляр класса
        """

        self.locator = f'//span[contains(text(), "{self.name}")]'
        return self

    def __open(self) -> WebElement:
        """
        Находит и возвращает элемент формы.

        :return: веб-элемент формы.
        """

        element = self.find_element()
        return element

    def count_inputs(self) -> int:
        """
        Находит и считает все видимые инпуты формы.

        :return: количество найденных элементов
        """

        locator = '//input[not(@type="hidden")]'
        elements = self.find_multiple_elements(locator)
        return len(elements)
