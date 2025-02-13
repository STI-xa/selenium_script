from pages.form_2_page import Form2Page
from test.test_base import BaseTestCase


class TestForm2(BaseTestCase):
    """Класс для тестирования веб-страницы Вебстраница_2."""
    page_class = Form2Page
    """класс страницы"""

    def test_operation_form(self) -> None:
        """Метод тестирует заполнение/обновление/удаление данных в
        форме Форма_2."""

        self.page.open()
        self.page.table.row(Название='test').double_click()
        self.page.add_button.click()
        self.page.form.name.set_value('test_1')
        self.page.form.field_1.set_value('SRID=5643;'
                                         'POLYGON((1 1,2 2,2 2,2 2,1 1))')

        self.page.save_button.click()
        assert self.page.form.name.get_value() == 'test_1', \
            'Значение инпута "Наименование" не совпадает с введеными'
        self.page.get_param('uuid')
        self.page.refresh()
        self.page.form.name.set_value('test_2')
        self.page.add_button.click()
        self.page.save_button.click()
        assert self.page.form.name.get_value() == 'test_2', \
            'Значение инпута "Наименование" не совпадает с обновленным'
        self.page.delete_button.click()
        self.page.save_button.click()
