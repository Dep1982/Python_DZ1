# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Введите число дня недели от 1 до 7: '))
if a==6 or a==7:
    print('Это выходной день')
else:
    print('Это не выходной день')
