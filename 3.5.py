
def my_summ():
    result = 0
    while True:
        user_answer = input('Введите несколько чисел через пробел или напечатайте "EXIT": ').upper()
        if user_answer == 'EXIT':
            break


        res = 0
        user_answer = user_answer.split()
        for letter in range(len(user_answer)):
            if user_answer[letter] == 'EXIT':
                break
            else:
                res = res + int(user_answer[letter])
            result = result + res
        print('Cумма чисел равна:', result)
    print('Итоговая сумма чисел равна:', result)


my_summ()
