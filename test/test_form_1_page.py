from pages.form_1_page import Form1Page
from test.test_base import BaseTestCase


class TestForm1(BaseTestCase):
    """Класс для тестирования веб-страницы Вебстраница_1."""
    page_class = Form1Page
    """класс страницы"""

    def test_form_1_with_altitude_field_visibility(self) -> None:
        """
        Проверяет возможность выбора значения из выпадающего списка для поля
        Тип_1.
        Проверяет наличие и отображенние инпутов из списка и проверяет,
        что количество полей соответствует количеству инпутов в списке в
        форме Форма_1 с обязательным полем Высота.
        """

        inputs = ['field_1', 'name', 'coordinates', 'altitude']

        self.page.open(operation='f5f545b2-a504-4c72-b1d7-7d75bbef046d')
        self.page.form.field_1.set_value('Тип 1')
        self.assertFormInputs(form=self.page.form, inputs_list=inputs)
        self.assertValueEqual(value=self.page.form.count_inputs(),
                              expected_value=len(inputs),
                              msg='Количество полей в форме Форма_1 должно '
                                  'быть 4')

    def test_form_1_without_altitude_field_visibility(self) -> None:
        """
        Проверяет возможность выбора значения из выпадающего списка для поля
        Тип_1.
        Проверяет наличие и отображенние инпутов из списка и проверяет,
        что количество полей соответствует количеству инпутов в списке в форме
        Форма_1 без поля Высота.
        """

        inputs = ['field_1', 'name', 'coordinates']

        self.page.open(operation='f5f545b2-a504-4b72-b1d7-7d75bbef045d')
        self.page.form.field_1.set_value('Тип 2')
        self.assertFormInputs(form=self.page.form, inputs_list=inputs)
        self.assertValueEqual(value=self.page.form.count_inputs(),
                              expected_value=len(inputs),
                              msg='Количество полей в форме Форма_1 '
                                  'надводного типа должно быть 3')
