"""
 Реализовать функцию, принимающую два числа (позиционные аргументы)
 и выполняющую их деление. Числа запрашивать у пользователя,
 предусмотреть обработку ситуации деления на ноль.
"""
def div_of_numbers(num_one, num_two):
    """
    :param num_one: запрашиваемое число
    :param num_two: запрашиваемое число
    :return: результат деления чисел
    """
    try:
        return round(num_one / num_two, 2)
    except ZeroDivisionError:
        return "Деление на 0!"

try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    print(
        f'Результат деления первого числа на второе: '
        f'{div_of_numbers(x, y)}')
    print(
        f'Результат деления второго числа на первое: '
        f'{div_of_numbers(y, x)}')
except ValueError:
    print("Вы ввели текст или символ. Вводите числа")