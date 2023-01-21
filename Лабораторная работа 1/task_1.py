import doctest
from typing import Union


class StarShip:
    def __init__(self, speed_volume: Union[int, float], propellant_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Космический корабль"
        :param speed_volume: Скорость корабля в км/ч
        :param propellant_volume: Объем имеющегося топлива в литрах
        Примеры:
        >>> starship = StarShip(1050, 0)  # инициализация экземпляра класса
        """
        if not isinstance(speed_volume, (int, float)):
            raise TypeError("Скорость корабля должна быть типа int или float")
        if speed_volume < 0:
            raise ValueError("Cкорость корабля не должна быть отрицательным числом")
        self.speed_volume = speed_volume

        if not isinstance(propellant_volume, (int, float)):
            raise TypeError("Объем имеющегося топлива должен быть int или float")
        if propellant_volume < 0:
            raise ValueError("Объем имеющегося топлива не может быть отрицательным числом")
        self.propellant_volume = propellant_volume

    def is_propellant_out(self) -> bool:
        """
        Функция, которая проверяет, закончилось ли топливо
        :return: Закончилось ли топливо
        Примеры:
        >>> starship = StarShip(1050, 0)
        >>> starship.is_propellant_out()
        """
        ...

    def hyperdrive(self, speed: Union[int, float]) -> None:
        """
        Увеличение скорости корабля во время гиперпрыжка
        :param speed: Величина добавляемой скорости
        :raise ValueError: Если добавляемая скорость меньше скорости света, то вызываем ошибку
        Примеры:
        >>> starship = StarShip(1500, 0)
        >>> starship.hyperdrive(1080000000)
        """
        if not isinstance(speed, (int, float)):
            raise TypeError("Добавляемая скорость должна быть типа int или float")
        if speed < 1079252848.8:
            raise ValueError("Добавляемая скорость должна быть больше скорости света")
        ...

    def propellant_refueling(self, propellant: Union[int, float]) -> Union[int, float]:
        """
        Заправка топлива.
        :param propellant: Объем заправляемого топлива
        :raise ValueError: Если количество заправляемого топлива превышает объем бака,
        то возвращается ошибка.
        :return: Объем реально заправленного топлива
        Примеры:
        >>> starship = StarShip(1500, 0)
        >>> starship.propellant_refueling(200)
        """
        ...


class DeathStar:
    def __init__(self, power_volume: Union[int, float], theft_of_plans: bool):
        """
        Создание и подготовка к работе объекта "Звезда смерти"
        :param power_volume: Мощность звезды смерти в процентах
        :param theft_of_plans: Украдены ли чертежы звезды смерти
        Примеры:
        >>> deathstar = DeathStar(100, True)  # инициализация экземпляра класса
        """
        if not isinstance(power_volume, (int, float)):
            raise TypeError("Мощность звезды смерти должна быть типа int или float")
        if power_volume < 0:
            raise ValueError("Мощность звезды смерти не должна быть отрицательным числом")
        self.power_volume = power_volume

        if not isinstance(theft_of_plans, bool):
            raise TypeError("Данный параметр должен быть bool")
        self.theft_of_plans = theft_of_plans

    def is_shoot_ready(self) -> bool:
        """
        Функция, которая проверяет, готова ли звезда смерти к выстрелу
        :return: Готова ли к выстрелу
        Примеры:
        >>> deathstar = DeathStar(100, False)
        >>> deathstar.is_shoot_ready()
        """
        ...

    def power_raise(self, power: Union[int, float]) -> None:
        """
        Увеличение мощности звезды смерти перед выстрелом
        :param power: Величина добавляемой мощности в процентах
        :raise ValueError: Если добавляемая мощность меньше нуля, то вызываем ошибку
        Примеры:
        >>> deathstar = DeathStar(100, False)
        >>> deathstar.power_raise(50)
        """
        if not isinstance(power, (int, float)):
            raise TypeError("Добавляемая мощность должна быть типа int или float")
        if power < 0:
            raise ValueError("Добавляемая мощность должна быть больше 0")
        ...

    def probability_of_destruction(self) -> Union[int, float]:
        """
        Проверяет возможность разрушения Звезды Смерти из-за кражи чертежей
        :return: Вероятность разрушения Звезды Смерти в процентах
        Примеры:
        >>> deathstar = DeathStar(0, True)
        >>> deathstar.probability_of_destruction()
        """
        ...


class Jedi:
    def __init__(self, jedi_number: Union[int, float], rebel_base_location: str):
        """
        Создание и подготовка к работе объекта "Орден Джедаев"
        :param jedi_number: Число членов ордена
        :param rebel_base_location: Расположение (планета) базы повстанцев
        Примеры:
        >>> jedi = Jedi(1, "Эндор")  # инициализация экземпляра класса
        """
        if not isinstance(jedi_number, (int, float)):
            raise TypeError("Параметр должен быть типа int или float")
        if jedi_number < 0:
            raise ValueError("Параметр не должен быть отрицательным числом")
        self.jedi_number = jedi_number

        if not isinstance(rebel_base_location, str):
            raise TypeError("Данный параметр должен быть str")
        self.rebel_base_locations = rebel_base_location

    def order_66(self) -> Union[int, float]:
        """
        Функция выдает число выживших джедаев после приказа 66
        :return: Число выживших
        Примеры:
        >>> jedi = Jedi(100, "Хот")
        >>> jedi.order_66()
        """
        ...

    def base_relocation(self) -> str:
        """
        Изменение расположение базы повстанцев (смена планеты)
        :return: Новое расположение базы повстанцев
        Примеры:
        >>> jedi = Jedi(2, "Дантуин")
        >>> jedi.base_relocation()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass

