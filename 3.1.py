
def my_function(a, b):
    if b == 0:
        return 'Нельзя делить на ноль'
    else:
        return a / b

number1 = int(input('Введи число 1: '))
number2 = int(input('Введи число 2: '))
print(f'Результат деление чисел: {my_function(number1, number2)}')