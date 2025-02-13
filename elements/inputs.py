from typing import Optional, Tuple, Union

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from elements.base import Base
from elements.buttons import Button


class BaseInput(Base):
    """Класс предоставляет базовые методы для работы с инпутами."""
    def _set_locator(self) -> 'BaseInput':
        """
        Метод устанавливает локатор инпута на основе полученного названия.

        :return: Возвращает текущий экземпляр класса
        """

        self.locator = (f'//input[@class="dx-texteditor-input"]/preceding::'
                        f'label//span[contains(text(), "{self.name}")]')
        return self

    def get_value(self) -> Optional[Union[str, int, list, dict]]:
        """
        Получает данные из инпута, соответствующие переданому названию.

        :return: значение инпута
        """

        element = self.find_element()
        element_value = element.get_property('value')
        return element_value

    def set_value(self,
                  value: Optional[Union[str, int, list, dict]]) -> 'BaseInput':
        """
        Вводит данные в инпут.

        :param value: Данные для ввода в инпут
        :return: возвращает текущий экземпляр класса
        """

        element = self.find_element()
        self.clean(element)
        element.send_keys(value)
        return self

    def clean(self, element) -> 'BaseInput':
        """Выбирает все значения в поле и удаляет их.

        :return: Возвращает текущий экземпляр класса
        """

        element.send_keys(Keys.CONTROL, 'a')
        # метод Селениума выделяет все значения в поле
        element.send_keys(Keys.BACKSPACE)
        # метод Селениума удаляет значения
        return self


class StrInput(BaseInput):
    """Класс предоставляет методы для взаимодействия со строковым инпутом."""
    pass


class DropdownListElement(BaseInput):
    """Класс предоставляет методы для взаимодействия с элементом из
    выпадающего списка."""
    def _set_locator(self, value: str = None) -> 'DropdownListElement':
        """Метод устанавливает локатор элмента из выпадающего списка на основе
        полученного значения.

        :param value: Название элемента для поиска в выпадающем списке
        :return: возвращает теккущий экземпляр класса
        """

        self.locator = ('//div[@class="dx-item-content dx-list-item-content" '
                        'and contains(text(), "{}")]').format(value)
        return self

    def find(self, value: str) -> 'WebElement':
        """
        Находит и возвращает элемент из выпадающего списка.

        :param value: Название элемента для поиска в выпадающем списке
        :return: веб-элемент списка.
        """
        self._set_locator(value)
        element = self.find_element()
        return element


class SelectInput(BaseInput):
    """Класс предоставляет методы для взаимодействия с инпутом из выпадающего
    списка."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dropdown_list_element = DropdownListElement(*args, parent=self)
        """Элемент из выпадающего списка"""

    def set_value(self, value: str) -> 'SelectInput':
        """
        Вводит данные в инпут.

        :param value: Данные для ввода в инпут
        :return: возвращает текущий экземпляр класса
        """

        element = self.find_element()
        element.click()
        dropdown_element = self.dropdown_list_element.find(value)
        dropdown_element.click()
        return self


class IntInput(BaseInput):
    """Класс предоставляет методы для взаимодействия со числовым инпутом."""
    pass


class GeometryInput(BaseInput):
    """Класс предоставляет методы для взаимодействия с инпутом ввода координат
    точки"""

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует объект инпута ввода координат, устанавливает долготу,
         широту и кнопку Показать на карте"""
        super().__init__(*args, **kwargs)
        self.longitude = Longitude(*args, parent=self)
        """Строка с данными долготы"""

        self.latitude = Latitude(*args, parent=self)
        """Строка с данными широты"""

        self.draw_on_map_button = Button(*args, parent=self, name='Показать '
                                                                  'на карте')
        """Кнопка в инпуте для отрисовки точки на карте"""

    def set_longitude_coordinates(self, coord: str) -> 'GeometryInput':
        """Метод устанавливает координаты долготы

        :param coord: координаты долготы в строковом формате
        :return: возвращает текущий экземпляр класса
        """
        degrees, minutes, seconds = self.pars_coordinates(coord)
        self.find_element()
        self.longitude.degrees.set_value(degrees)
        self.longitude.minutes.set_value(minutes)
        self.longitude.seconds.set_value(seconds)
        return self

    def set_latitude_coordinates(self, coord: str) -> 'GeometryInput':
        """Метод устанавливает координаты широты

        :param coord: координаты широты в строковом формате
        :return: возвращает текущий экземпляр класса
        """
        degrees, minutes, seconds = self.pars_coordinates(coord)
        self.find_element()
        self.latitude.degrees.set_value(degrees)
        self.latitude.minutes.set_value(minutes)
        self.latitude.seconds.set_value(seconds)
        return self

    def pars_coordinates(self, coord: str) -> Tuple[int, int, int]:
        parts = coord.split(',')
        degrees, minutes, seconds = map(int, parts)
        return degrees, minutes, seconds


class Longitude(BaseInput):
    """Класс представляет строку Долгота."""
    name = 'Долгота'
    """название строки"""

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует объект строки ввода координат Долготы."""
        super().__init__(*args, **kwargs)
        self.degrees = Coordinate(*args, parent=self, name='Градусы')
        """ячейка для ввода значения градусов"""

        self.minutes = Coordinate(*args, parent=self, name='Минуты')
        """ячейка для ввода значения минут"""

        self.seconds = Coordinate(*args, parent=self, name='Секунды')
        """ячейка для ввода значения секунд"""

    def _set_locator(self) -> 'Longitude':
        """
        Метод устанавливает локатор ячейки строки Долгота на основе заданного
        названия.

        :return: Возвращает текущий экземпляр класса
        """

        self.locator = (f'//following::dms-form/preceding::span[@title="'
                        f'{self.name}"]')
        return self


class Latitude(BaseInput):
    """Класс представляет строку Широта."""
    name = 'Широта'
    """название строки"""

    def __init__(self, *args, **kwargs) -> None:
        """Инициализирует объект строки ввода координат Широты."""
        super().__init__(*args, **kwargs)
        self.degrees = Coordinate(*args, parent=self, name='Градусы')
        """ячейка для ввода значения градусов"""

        self.minutes = Coordinate(*args, parent=self, name='Минуты')
        """ячейка для ввода значения минут"""

        self.seconds = Coordinate(*args, parent=self, name='Секунды')
        """ячейка для ввода значения секунд"""

    def _set_locator(self) -> 'Latitude':
        """
        Метод устанавливает локатор ячейки строки Широта на основе заданного
        названия.

        :return: Возвращает текущий экземпляр класса
        """
        self.locator = (f'//following::dms-form/preceding::span[@title="'
                        f'{self.name}"]')
        return self


class Coordinate(BaseInput):
    """Класс предоставляет методы для взаимодействия со числовым инпутом."""

    def _set_locator(self) -> 'Coordinate':
        """
        Метод устанавливает локатор инпута на основе полученного названия.

        :return: Возвращает текущий экземпляр класса
        """

        self.locator = (f'following::dx-number-box[@title="{self.name}"]//'
                        f'input[@inputmode="decimal"]')
        return self
