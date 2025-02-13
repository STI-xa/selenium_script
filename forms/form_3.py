from elements.base_form import BaseFormHandler
from elements.inputs import StrInput, IntInput, GeometryInput


class Form3Handler(BaseFormHandler):
    """Класс представляющий форму Форма_3."""

    name = 'Форма_3'
    """название формы"""

    def __init__(self, *args,  **kwargs) -> None:
        """Инициализирует объект формы Форма_3."""
        super().__init__(*args, **kwargs)

        self.name = StrInput(*args, parent=self, name='Наименование')
        """Инпут для ввода данных поля Наименование"""

        self.point = GeometryInput(*args, parent=self, name='Точка')
        """Инпут для ввода данных поля Точка"""

        self.altitude = IntInput(*args, parent=self, name='Высота')
        """Инпут для ввода данных поля Высота"""

        self.radius = IntInput(*args, parent=self, name='Радиус')
        """Инпут для ввода данных поля Радиус"""
