# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:

# - x=34; y=-30-> 4
# - x=2; y=4-> 1
# - x=-34; y=-30-> 3

# x = int(input('Введите значение координаты x: '))
# y = int(input('Введите значение координаты y: '))


# def checkValue(x):
#     if x or y == 0:
#         print(f"Координаты не могут равняться 0")


# def checkQuarter(xy):
#     quarter = 4
#     if x > 0 and y > 0:
#         quarter = 1
#     elif x > 0 and y < 0:
#         quarter = 2
#     elif x < 0 and y < 0:
#         quarter = 3
#     print(f"Точка находится в {quarter} четверти плоскости")


# cordinate = checkValue(x)
# checkQuarter(cordinate)

x = int(input('Введите значение координаты x: '))
y = int(input('Введите значение координаты y: '))


def checkValue(x, y):
    if (x == 0) or (y == 0):
        print(f"Координаты не могут равняться 0")


def checkQuarter(x, y):
    quarter = 4
    if x > 0 and y > 0:
        quarter = 1
    elif x > 0 and y < 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    print(f"Точка находится в {quarter} четверти плоскости")


cordinate = checkValue(x, y)
if (x != 0) and (y != 0):
    checkQuarter(x, y)
