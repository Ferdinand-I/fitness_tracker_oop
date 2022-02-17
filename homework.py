from __future__ import annotations
from typing import List, Optional


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Получить информационное сообщение о пройденноё тренировке."""
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action: int = action
        self.duration: float = duration
        self.weight: float = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / Training.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NameError('NotImplementedError')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(training_type=self.__class__.__name__,
                           duration=self.duration,
                           distance=self.get_distance(),
                           speed=self.get_mean_speed(),
                           calories=self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        return ((Running.COEFF_CALORIE_1 * self.get_mean_speed()
                 - Running.COEFF_CALORIE_2)
                * self.weight / self.M_IN_KM * self.duration * 60)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEFF_CALORIE_1 = 0.035
    COEFF_CALORIE_2 = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight
                         )
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        return ((SportsWalking.COEFF_CALORIE_1 * self.weight
                + (self.get_mean_speed()**2 // self.height)
                * SportsWalking.COEFF_CALORIE_2 * self.weight)
                * self.duration * 60)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    COEFF_CALORIE_1: float = 1.1
    COEFF_CALORIE_2: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        return ((self.get_mean_speed() + Swimming.COEFF_CALORIE_1)
                * Swimming.COEFF_CALORIE_2 * self.weight)


workout_dict = {'RUN': Running, 'WLK': SportsWalking, 'SWM': Swimming}


def read_package(workout_type: str, data: List[int]) -> Optional[Training]:
    """Прочитать данные полученные от датчиков."""
    if workout_type in workout_dict:
        return workout_dict[workout_type](*data)
    else:
        return None


def main(sports: Optional[Training]) -> None:
    """Главная функция."""
    if sports is None:
        print('Нет такой тренировки.')
    else:
        info = sports.show_training_info()
        print(info.get_message())


if __name__ == '__main__':

    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for arg_1, arg_2 in packages:
        training = read_package(arg_1, arg_2)
        main(training)
