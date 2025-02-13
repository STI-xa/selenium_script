from elements.base_form import BaseFormHandler
from elements.inputs import StrInput


class Form2Handler(BaseFormHandler):
    """Класс представляющий форму Форма_2."""

    name = 'Форма_2'
    """название формы"""

    def __init__(self, *args,  **kwargs) -> None:
        """Инициализирует объект формы Форма_2."""
        super().__init__(*args, **kwargs)

        self.name = StrInput(*args, parent=self, name='Наименование')
        """Инпут для ввода данных поля Наименование"""

        self.field_1 = StrInput(*args, parent=self, name='Поле_1')
        """Инпут для ввода данных поля Поле_1"""

        self.field_2 = StrInput(*args, parent=self, name='Поле_2')
        """Инпут для ввода данных поля Поле_2"""
