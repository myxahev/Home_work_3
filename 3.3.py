def min_list(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    print('Сумма наибольших двух аргументов равна:', sum(my_list))

user_num1 = int(input("Введите первое число: "))
user_num2 = int(input("Введите второе число: "))
user_num3 = int(input("Введите третье число: "))
min_list(user_num1, user_num2, user_num3)