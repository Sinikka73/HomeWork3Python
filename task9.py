"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой 
считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
def my_func(arr):
    """
    Функция перемножает крайние элементы списка
    :param arr: список чисел. Задаётся в программе
    :return: возвращает список с результатом
    """
    my_lst = []
    for i in range(0, len(arr) // 2):
        my_lst.append(arr[i] * arr[- i - 1])
    if len(arr) % 2 != 0:
        my_lst.append(arr[len(my_lst) // 2] * arr[len(my_lst) // 2])
    return my_lst

lst_1, lst_2 = [2, 3, 4, 5, 6], [2, 3, 5, 6]
print(f'{lst_1} => {my_func(lst_1)}')
print(f'{lst_2} => {my_func(lst_2)}')
