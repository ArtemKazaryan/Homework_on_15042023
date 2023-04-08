

# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!


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

# Пример для ввода:
# Mazda 6, 2017, Mazda Motor Corporation, 2.0, red, 16000

print()
print('------------------')
print('Решение задания №1')
print('------------------')

class Car:
    def __init__(self, car_model, year_of_manufacture, manufacturer,
                 engine_capacity, car_color, price):
        self.car_model = car_model
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.car_color = car_color
        self.price = price

    def set_car_info(self):
        self.car_model = input('Введите название модели автомобиля: ')
        self.year_of_manufacture = input('Введите год выпуска: ')
        self.manufacturer = input('Введите производителя: ')
        self.engine_capacity = input('Введите объем двигателя, л: ')
        self.car_color = input('Введите цвет автомобиля: ')
        self.price = input('Введите цену, $: ')
        print()

    def print_car_info(self):
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

car.print_car_info()
car.set_car_info()
car.print_car_info()



# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в
# полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.
#
# Решение:

# Пример для ввода:
# Ася, 1858, журнал «Современник», повесть, Иван Тургенев, 250

print()
print('------------------')
print('Решение задания №2')
print('------------------')

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
        self.price = input('Введите цену, руб.: ')
        print()

    def print_book_info(self):
        print(f'Название книги: {self.book_title}')
        print(f'Год выпуска: {self.year_of_release}')
        print(f'Издатель: {self.publisher}')
        print(f'Жанр: {self.genre}')
        print(f'Автор: {self.author}')
        print(f'Цена, руб.: {self.price}')
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

# Пример для ввода:
# «Сантьяго Бернабеу», 14.12.1947, Испания, Мадрид, 75000

print()
print('------------------')
print('Решение задания №3')
print('------------------')

class Stadium:
    def __init__(self, stadium_name, opening_date, country, city, capacity):
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def set_stadium_info(self):
        self.stadium_name = input('Введите название стадиона: ')
        self.opening_date = input('Введите дату открытия: ')
        self.country = input('Введите страну расположения: ')
        self.city = input('Введите город расположения: ')
        self.capacity = input('Введите вместимость стадиона, чел.: ')
        print()

    def print_stadium_info(self):
        print(f'Название стадиона: {self.stadium_name}')
        print(f'Дата открытия: {self.opening_date}')
        print(f'Страна расположения: {self.country}')
        print(f'Город расположения: {self.city}')
        print(f'Вместимость, чел.: {self.capacity}')
        print()

stadium = Stadium(stadium_name='Неопределено', opening_date='Неопределена',
          country='Неопределена', city='Неопределён',
          capacity='Неопределена')

stadium.print_stadium_info()
stadium.set_stadium_info()
stadium.print_stadium_info()