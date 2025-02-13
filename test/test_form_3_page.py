from time import sleep

from pages.form_3_page import Form3Page
from test.test_base import BaseTestCase


class TestForm3(BaseTestCase):
    """Класс для тестирования веб-страницы Вебстраница_3."""
    page_class = Form3Page
    """класс страницы"""

    def test_form_3_create(self) -> None:
        """Метод тестирует создание новой записи в форме Форма_3."""
        self.page.open()
        self.page.table.create_button.click()
        self.page.form.name.set_value('test_1')
        self.page.form.point.set_longitude_coordinates('21,28,15')
        self.page.form.point.set_latitude_coordinates('21,23,45')
        self.page.form.point.draw_on_map_button.click()
        self.page.form.altitude.set_value('666')
        self.page.form.radius.set_value('999')
        self.page.add_button.click()
        self.page.save_button.click()
        self.page.update_button.click()
        self.page.table.row(Название='test_1').double_click()

    def test_form_3_edit(self) -> None:
        """Метод тестирует изменение данных в уже созданной записи в
        форме Форма_3."""

        self.page.open()
        self.page.table.row(Название='test_1').double_click()
        self.page.form.name.set_value('test_2')
        self.page.form.altitude.set_value('555')
        self.page.add_button.click()
        self.page.save_button.click()
        self.page.update_button.click()
        self.page.table.row(Название='test_2').double_click()
        self.assertValueEqual(value=self.page.form.name.get_value(),
                              expected_value='test_2',
                              msg='Данные в поле Наименование не '
                                  'совпадают с введенными')

    def test_form_3_delete(self) -> None:
        """Метод тестирует удаление созданной записи в форме Форма_3."""
        self.page.open()
        self.page.table.row(Название='test_2', Радиус=999).double_click()
        self.page.delete_button.click()
        self.page.save_button.click()

    def test_new_option(self):
        self.page.open()
        sleep(3)
        self.page.table.row(Название='test').double_click()
        self.page.table.create_button.click()
        self.page.form.point.set_longitude_coordinates('21,28,15')
        self.page.form.point.set_latitude_coordinates('21,23,45')
        self.page.form.altitude.set_value('666')
