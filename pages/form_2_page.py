from elements.tables import Table
from pages.base_page import BasePage
from forms.form_2 import Form2Handler
from elements.buttons import Button


class Form2Page(BasePage):
    """Класс для работы со страницей формы Форма_2."""

    url = '/form_2'
    """URL страницы"""

    def __init__(self, *args) -> None:
        """Инициализирует объект страницы формы Форма_2."""

        super().__init__(*args)
        self.form = Form2Handler(*args)
        """Форма Форма_2"""

        self.table = Table(*args)
        """Таблица со списком наименований"""

        self.save_button = Button(*args, name='Сохранить')
        """Кнопка Сохранить"""

        self.add_button = Button(*args, name='Редактировать')
        """Кнопка Редактировать"""

        self.delete_button = Button(*args, name='Удалить')
        """Кнопка Удалить"""
