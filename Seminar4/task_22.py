# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


N = int(input("Введите количество элементов в массиве N: "))
M = int(input("Введите количество элементов в массиве M: "))
first = []
for i in range (N):
    first.append(input(f"Введите {i} элемент множества: "))
print(first)
second = []
for i in range (M):
    second.append(input(f"Введите {i} элемент множества: "))
print(second)
unique_first = set(first)
unique_second = set(second)
sum = unique_first.intersection(unique_second)
print(sum)
result = list(sum)
result.sort()
print(f"отсортированные числа , которые встречаются в обоих списках: {result}")