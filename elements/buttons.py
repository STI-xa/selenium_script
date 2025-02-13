from elements.base import Base


class Button(Base):
    """Базовый класс предоставляет методы для взаимодействия с кнопками."""

    name: str = ...

    def _set_locator(self) -> 'Button':
        """
        Метод устанавливает локатор кнопки на основе переданного названия.

        :return self: возвращает теккущий экземпляр класса
        """
        self.locator = (
            f'//div[@class="dx-button-content"]/span[contains(text(),'
            f' "{self.name}")] | //div[@title="{self.name}"] | '
            f'//dx-button[@title="{self.name}"] | '
            f'//dx-button[@aria-label="{self.name}"]'
        )
        return self

    def click(self) -> 'Button':
        """
        Находит и кликает кнопку.

        :return self: возвращает текущий экземпляр класса
        """

        button = self.find_element()
        button.click()
        return self
