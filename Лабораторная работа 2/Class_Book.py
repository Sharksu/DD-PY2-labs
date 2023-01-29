from pydantic import BaseModel, conint

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

    def __repr__(self) -> str:
        """
        Магические метод __repr__
        :return: Валидная python строка, по которой можно инициализировать точно такой же экземпляр
        """
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

