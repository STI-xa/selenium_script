from elements.base_form import BaseFormHandler
from elements.inputs import StrInput, SelectInput, IntInput


class Form1Handler(BaseFormHandler):
    """Класс представляющий форму Форма_1."""

    name = 'Форма_1'
    """название формы"""

    def __init__(self, *args,  **kwargs) -> None:
        """Инициализирует объект формы Форма_1."""
        super().__init__(*args, **kwargs)

        self.type_1 = SelectInput(*args,
                                  parent=self,
                                  name='Тип_1')
        """Инпут с выпадающим списком поля Тип_1"""

        self.name = StrInput(*args, parent=self, name='Наименование')
        """Инпут для ввода данных поля Наименование"""

        self.coordinates = StrInput(*args, parent=self, name='Координаты')
        """Инпут для ввода данных поля Координаты"""

        self.altitude = IntInput(*args, parent=self, name='Высота')
        """Инпут для ввода данных поля Высота"""
