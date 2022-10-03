# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

user_number = float(input('Введите число: '))
length_of_user_number = len(str(user_number)) 
our_number = user_number * 10 ** (length_of_user_number - 2)
sum = 0
while our_number > 0:
    sum = sum + our_number % 10
    our_number = our_number // 10
print('Сумма цифр числа ', user_number, 'равна', sum)