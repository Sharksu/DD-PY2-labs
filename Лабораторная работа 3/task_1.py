class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        """ Магический метод __str__. """
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        """ Магический метод __repr__. """
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        """Возвращает имя книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author


class PaperBook(Book):
    """Дочерний класс - Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        """ Магический метод __str__. Перегружаем, поскольку добавляется новая информация - число страниц"""
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self) -> str:
        """ Магический метод __repr__. Перегружаем, поскольку добавляется новая информация - число страниц"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self.pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = new_pages


class AudioBook(Book):
    """Дочерний класс - аудио книга"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        """ Магический метод __str__. Перегружаем, поскольку добавляется новая информация - длительность"""
        return f"Книга {self._name}. Автор {self._author}. Длительность {self.duration}"

    def __repr__(self) -> str:
        """ Магический метод __repr__. Перегружаем, поскольку добавляется новая информация - длительность"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        """Возвращает длительность книги."""
        return self.duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает длительность книги."""
        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self.duration = new_duration

