def func_v(x, y):
    print(x ** y)

def func_g(x, y):
    y = abs(y)
    result = x
    for i in range(y-1):
        result *= x
    result = 1 / result
    print(result)

user_num1 = int(input("Введите первое число: "))
user_num2 = int(input("Введите второе число: "))
func_v(user_num1, user_num2)
func_g(user_num1, user_num2)