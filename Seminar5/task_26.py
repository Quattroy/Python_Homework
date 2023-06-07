# Задача 26:  Напишите программу, которая на вход принимает два числа 
# A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def number_to_power(number, power):
    if power == 0:
        return 1
    return number * number_to_power(number, power - 1)


print(number_to_power(5, 2))
