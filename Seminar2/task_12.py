# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
#  а Катя должна их отгадать. Для этого Петя делает две подсказки. 
#  Он называет сумму этих чисел S и их произведение P. 
#  Помогите Кате отгадать задуманные Петей числа.

summ = int(input("Введите сумму чисел S: "))
multiplication = int(input("Введите произведение чисел P: "))
x = 0
y = 0
for x in range(1, 1000, 1):
    for y in range(1, 1000, 1):
        if (x + y) == summ and (x * y) == multiplication:
            print(f"Задуманные Петей числа с суммой = {summ} и произведением = {multiplication} : X = {x}, Y = {y} ")
            break
        else:
            print(f"Введенным сумме и произведению чисел не возможно подобрать соотвествующие натуральные числа")
            break
    break
