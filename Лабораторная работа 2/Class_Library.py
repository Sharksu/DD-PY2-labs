from pydantic import BaseModel, conint
from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    """
        Создание класса "Книга"
        :param id_: Идентификатор книги
        :param name:  Название книги
        :param pages:  Количество страниц в книге
        """
    id_: conint(gt=0)
    name: str
    pages: conint(gt=0)

    def __str__(self) -> str:
        """
        Магические метод __str__
        :return: Строка формата, где "название_книги" берется с помощью атрибута name
        """
        return f'Книга "{self.name}"'


class Library(BaseModel):
    """
    Создание класса "<Библиотека>"
    :param books: Идентификатор книги
    """
    books: Optional[list] = []

    def get_next_book_id(self):
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        :return: id новой книги
        """
        return len(self.books) + 1

    def get_index_by_book_id(self, id_: int):
        """
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :return: Индекс книги по id
        """
        index = [j for j, i in enumerate(self.books) if i.id_ == id_]  # Допустим, id - это не просто порядковый номер
        if len(index) == 0:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            return index[0]


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

