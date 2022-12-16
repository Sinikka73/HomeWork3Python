"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def personal_information(name_2, year, place, email, phone):
    """
    :param name_2: имя, фамилия
    :param year: год рождения
    :param place: город проживания
    :param email: электронный адрес
    :param phone: телефон
    :return:
    """
    print(f"{name_2} {year}г.р., проживает в городе {place}, "
          f"e-mail: {email}, тел.: {phone}")


personal_information(name_2="Александра Сергеева",
                     year="1991", place="Москва",
                     email="alex@mail.ru", phone="+79218833888")