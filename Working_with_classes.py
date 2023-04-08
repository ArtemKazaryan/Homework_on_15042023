

# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ  !!!!!!


# Домашняя работа на 15.04.2023.


# Модуль 10. Объектно-ориентированное
# программирование
# Тема: Классы. Объекты. Часть 1


# Задание 1
# Реализуйте класс «Автомобиль». Необходимо хранить
# в полях класса: название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте
# методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса
#
# Решение:
class Car:
    def __init__(self, car_model, year_of_manufacture, manufacturer,
                 engine_capacity, car_color, price):
        self.car_model = car_model
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.car_color = car_color
        self.price = price

    def set_info(self):
        self.car_model = input('Введите название модели автомобиля: ')
        self.year_of_manufacture = input('Введите год выпуска: ')
        self.manufacturer = input('Введите производителя: ')
        self.engine_capacity = input('Введите объем двигателя, л: ')
        self.car_color = input('Введите цвет автомобиля: ')
        self.price = input('Введите цену, $: ')
        print()

    def print_info(self):
        print(f'Название модели автомобиля: {self.car_model}')
        print(f'Год выпуска: {self.year_of_manufacture}')
        print(f'Производитель: {self.manufacturer}')
        print(f'Объем двигателя, л: {self.engine_capacity}')
        print(f'Цвет автомобиля: {self.car_color}')
        print(f'Цена, $: {self.price}')
        print()

car = Car(car_model='Неопределена', year_of_manufacture='Неопределён',
          manufacturer='Неопределён', engine_capacity='Неопределён',
          car_color='Неопределён', price='Неопределена')

car.print_info()
car.set_info()
car.print_info()





# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
#
# Решение:
#

# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


# Решение: