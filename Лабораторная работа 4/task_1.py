import doctest


class Games:
    MAIN_CHARACTER = [{"game": "Half-Life", "character": "Гордон Фримен"},  # пример списка с именами главных героев
                      {"game": "Devil May Cry 3", "character": "Данте"},
                      {"game": "Resident Evil 4", "character": "Леон"},
                      {"game": "Little Nightmares", "character": "Шестая"},
                      {"game": "Dishonored", "character": "Корво Аттано"},
                      {"game": "Outer Wilds", "character": "Камелянин"}]

    def __init__(self, name: str, genre: str, cost: float):
        """ Базовый класс - Компьютерные игры
        :param name: Название компьютерной игры
        :param genre: Жанр компьютерной игры
        :param cost: Стоимость компьютерной игры
        Примеры:
        >>> game_1 = Games("Dishonored", "Стелс-экшен", 160.49)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название компьютерной игры должно быть типа str")
        self._name = name

        if not isinstance(genre, str):
            raise TypeError("Жанр компьютерной игры должен быть типа str")
        self._genre = genre

        if not isinstance(cost, float):
            raise TypeError("Стоимость компьютерной игры должна быть типа float")
        if cost < 0:
            raise ValueError("Стоимость компьютерной игры не должна быть отрицательным числом")
        self.cost = cost

    def __str__(self) -> str:
        """ Магический метод __str__. """
        return f"Игра {self._name}. Жанр {self._genre}. Стоимость {self.cost}"

    def __repr__(self) -> str:
        """ Магический метод __repr__. """
        return f"{self.__class__.__name__}(name={self._name!r}, genre={self._genre!r}, cost={self.cost!r})"

    def buy_a_game(self, money: float) -> float:
        """ Покупка игры в магазине
        :param money: Сколько денег имеется
        :raise TypeError: Если задан не тот тип данных, то вызываем ошибку
        :raise ValueError: Если денег отрицательное количество, то вызываем ошибку
        :return: Сдача
        Примеры:
        >>> game_1 = Games("Dishonored", "Стелс-экшен", 160.49)
        >>> game_1.buy_a_game(500.5)
        340.01
        """
        if not isinstance(money, float):
            raise TypeError("Количество денег должно быть типа float")
        if money < 0:
            raise ValueError("Количество денег не должно быть отрицательным числом")
        return money - self.cost

    def print_a_characters_name(self) -> str:
        """ Узнать имя главного персонажа игры
        :return: Имя главного персонажа игры
        Примеры:
        >>> game_1 = Games("Dishonored", "Стелс-экшен", 160.49)
        >>> game_1.print_a_characters_name()
        'Корво Аттано'
        """
        names = [i["character"] for i in self.MAIN_CHARACTER if i["game"] == self._name]
        return names[0]

    @property
    def name(self) -> str:
        """Возвращает название игры. Причина инкапсуляции: название игры не меняется после выхода"""
        return self._name

    @property
    def genre(self) -> str:
        """Возвращает жанр игры. Причина инкапсуляции: жанр игры не меняется после выхода"""
        return self._genre


class CoopGames(Games):
    def __init__(self, name: str, genre: str, cost: float, nickname: str):
        """Дочерний класс - кооперативные игры
        Магический метод __str__  и метод buy_a_game наследуем от базового класса - оставляем такие же выходные данные
        :param name: Название компьютерной игры
        :param genre: Жанр компьютерной игры
        :param cost: Стоимость компьютерной игры
        :param nickname: Ваш ник
        Примеры:
        >>> game_2 = CoopGames("Phasmophobia", "Хоррор на выживание", 309.1, "Sharksu")
        """
        super().__init__(name, genre, cost)

        if not isinstance(nickname, str):
            raise TypeError("Ваш ник должен быть типа str")
        self.nickname = nickname

    def __repr__(self) -> str:
        """ Магический метод __repr__. Перегружаем с добавлением новой информации"""
        return f"{self.__class__.__name__}(name={self._name!r}, genre={self._genre!r}, cost={self.cost!r}, " \
               f"nickname={self.nickname!r})"

    def print_a_characters_name(self) -> str:
        """ Узнать имя главного персонажа игры.
        Перегружаем, так как имя главного персонажа в таких играх - ваш ник
        :return: Имя главного персонажа игры
        Примеры:
        >>> game_2 = CoopGames("Phasmophobia", "Хоррор на выживание", 309.1, "Sharksu")
        >>> game_2.print_a_characters_name()
        'Добро пожаловать, Sharksu!'
         """
        return f"Добро пожаловать, {self.nickname}!"


if __name__ == "__main__":
    doctest.testmod()
    pass

