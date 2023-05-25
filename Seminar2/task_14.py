# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))
res = 0
k = 2
i = 1
while res < N:
    i += 1
    res = k ** i
    if k ** i > N:
        i -= 1
        res = k ** i
        break
print(N, res, i)
      