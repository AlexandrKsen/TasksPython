# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите день недели: '))
if day > 0 and day < 6:
    print("Это рабочий день")
elif day > 5 and day < 8:
    print("Это выходной")
else:
    print("Это не день недели")