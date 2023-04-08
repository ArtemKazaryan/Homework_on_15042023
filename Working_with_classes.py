

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
# class Car:
#     def __init__(self, car_model, year_of_manufacture, manufacturer,
#                  engine_capacity, car_color, price):
#         self.car_model = car_model
#         self.year_of_manufacture = year_of_manufacture
#         self.manufacturer = manufacturer
#         self.engine_capacity = engine_capacity
#         self.car_color = car_color
#         self.price = price
#
#     def set_car_info(self):
#         self.car_model = input('Введите название модели автомобиля: ')
#         self.year_of_manufacture = input('Введите год выпуска: ')
#         self.manufacturer = input('Введите производителя: ')
#         self.engine_capacity = input('Введите объем двигателя, л: ')
#         self.car_color = input('Введите цвет автомобиля: ')
#         self.price = input('Введите цену, $: ')
#         print()
#
#     def print_car_info(self):
#         print(f'Название модели автомобиля: {self.car_model}')
#         print(f'Год выпуска: {self.year_of_manufacture}')
#         print(f'Производитель: {self.manufacturer}')
#         print(f'Объем двигателя, л: {self.engine_capacity}')
#         print(f'Цвет автомобиля: {self.car_color}')
#         print(f'Цена, $: {self.price}')
#         print()
#
# car = Car(car_model='Неопределена', year_of_manufacture='Неопределён',
#           manufacturer='Неопределён', engine_capacity='Неопределён',
#           car_color='Неопределён', price='Неопределена')
#
# car.print_car_info()
# car.set_car_info()
# car.print_car_info()



# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
#
# Решение:
#
class Book:
    def __init__(self, book_title, year_of_release, publisher,
                 genre, author, price):
        self.book_title = book_title
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_book_info(self):
        self.book_title = input('Введите название книги: ')
        self.year_of_release = input('Введите год выпуска: ')
        self.publisher = input('Введите издателя: ')
        self.genre = input('Введите жанр: ')
        self.author = input('Введите автора: ')
        self.price = input('Введите цену, $: ')
        print()

    def print_book_info(self):
        print(f'Название книги: {self.book_title}')
        print(f'Год выпуска: {self.year_of_release}')
        print(f'Издателль: {self.publisher}')
        print(f'Жанр: {self.genre}')
        print(f'Автор: {self.author}')
        print(f'Цена, $: {self.price}')
        print()

book = Book(book_title='Неопределено', year_of_release='Неопределён',
          publisher='Неопределён', genre='Неопределён',
          author='Неопределён', price='Неопределена')

book.print_book_info()
book.set_book_info()
book.print_book_info()






# Задание 3
# Реализуйте класс «Стадион». Необходимо хранить в
# полях класса: название стадиона, дату открытия, страну,
# город, вместимость. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.


# Решение: