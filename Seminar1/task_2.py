# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите трехзначное число: "))
num1 = num % 10
num2 = num // 10 % 10
num3 = num // 100
result = num1 + num2 + num3
print(f"Суммы чисел: {num3} + {num2} + {num1}  =  {result}")