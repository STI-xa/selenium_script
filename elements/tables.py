from typing import Dict

from elements.base import Base
from elements.buttons import Button


class Table(Base):
    """Класс предоставляет методы для взаимодействия с таблицей"""
    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует объект таблицы."""
        super().__init__(*args, **kwargs)
        self.row = Row(*args, parent=self)
        """объект класса Row для работы со строками таблицы"""

        self.create_button = Button(*args, name='plus')
        """кнопка создания новой записи в таблице"""

    def _set_locator(self) -> 'Table':
        """
        Метод устанавливает локатор таблицы.

        :return: возвращает текущий экземпляр класса
        """
        self.locator = '//dx-data-grid//table'
        return self


class Row(Base):
    """Класс предоставляет методы для взаимодействия со строкой"""

    def __call__(self, **set_column_value: Dict[str, str]):
        """
        Метод устанавливает локатор на основе полученных аргументов, находит и
        возвращает объект доступный для двойного клика

        :return: возвращает текущий экземпляр класса
        """

        self._set_locator(**set_column_value)
        self.find_element()
        return self

    def _set_locator(self, **set_column_value: Dict[str, str]) -> 'Row':
        """
        Метод устанавливает локатор строки на основе полученных значений из
        словаря, если передано больше одного ключ=значение, то собирает
        локатор так, чтобы при поиске были заданы сразу все полученные
        значения в строке.

        :return: возвращает текущий экземпляр класса
        """

        conditions = [
            (f'td[@aria-colindex=//td[contains(@aria-label, "{column}")]'
             f'/@aria-colindex and text()="{value}"]')
            for column, value in set_column_value.items()]
        self.locator = f'//tr[{" and ".join(conditions)}]'
        return self

    def double_click(self):
        """Выполняет двойной клик по веб-элементу"""
        element = self.find_element()
        self.action.double_click(element).perform()
        return self
