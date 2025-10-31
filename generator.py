from random import randint

class Person: # Регистрационные данные для уникального пользователя
    user_name = 'Виктор'
    email = 'viktorprokopovich3131@ya.ru'
    password = 'qwerty1234'

class Random: # Регистрационные данные для рандомного пользователя
    user_name = 'test'
    email = f'test_user{randint(0, 9999)}@ya.ru'
    password = f'qwerty{randint(1000, 9999)}'