from pages.base_page import BasePage
from forms.form_1 import Form1Handler
from elements.buttons import Button


class Form1Page(BasePage):
    """Класс для работы со страницей формы Форма_1."""

    url = '/form_1'
    """URL страницы"""

    def __init__(self, *args) -> None:
        """Инициализирует объект страницы формы Форма_1."""

        super().__init__(*args)
        self.form = Form1Handler(*args)
        """Форма Форма_1"""

        self.save_button = Button(*args, name='Сохранить')
        """Кнопка Сохранить"""

        self.update_button = Button(*args, name='Обновить')
        """Кнопка Обновить"""

        self.cancel_button = Button(*args, name='Отмена')
        """Кнопка Отмена"""

        self.delete_button = Button(*args, name='Удалить')
        """Кнопка Удалить"""
