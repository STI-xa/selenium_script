from pages.base_page import BasePage
from forms.form_3 import Form3Handler
from elements.buttons import Button
from elements.tables import Table


class Form3Page(BasePage):
    """Класс для работы со страницей формы Форма_3."""

    url = '/form_3'
    """URL страницы"""

    def __init__(self, *args) -> None:
        """Инициализирует объект страницы формы Форма_3."""

        super().__init__(*args)
        self.form = Form3Handler(*args)
        """Форма Форма_3"""

        self.table = Table(*args)
        """Таблица со списком наименований"""

        self.save_button = Button(*args, name='Сохранить')
        """Кнопка Сохранить"""

        self.add_button = Button(*args, name='Добавить/Изменить')
        """Кнопка Добавить/Изменить"""

        self.update_button = Button(*args, name='Обновить')
        """Кнопка Обновить"""

        self.delete_button = Button(*args, name='Удалить')
        """Кнопка Удалить"""
