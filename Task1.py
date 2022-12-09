# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]  N = 30 -> [2, 3, 5]

from typing import List
def find_simple_miltiplier(new_list: List[int], n: int, simple_m: int) -> List[int]:
    '''
    Возвращает список, заполненный простыми множителями заданного числа

        Args:
            new_list (List[int]) - список
            n (int) - число, которое задаёт пользователь
            simple_m (int) - минимальный простой множитель
        Returns:
            new_list (List[int]) - список, заполненный простыми множителями заданного числа
    '''
    while n > 1:
        if n % simple_m == 0:
            n /= simple_m
            if simple_m not in new_list:
                new_list.append(simple_m)
        else:
            simple_m += 1

number = int(input("Введите натуральное число: "))
simple_multiplier = 2
n_list = []
init_num = number
find_simple_miltiplier(n_list, number, simple_multiplier)
print(f"У числа {init_num} следующие простые множители: {n_list}")
