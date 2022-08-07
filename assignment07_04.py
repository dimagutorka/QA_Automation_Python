# Завдання: написати програму обчислення факторіалу числа.
#           Программа запитує ввод від користувача у циклі
#           (вихід можливий за допомогою Ctrl-C/D)
# 
# Факторіал числа: n!
# n! = 1 * 2 * 3 * 4 ... n-1 * n
# 0! = 1
#
# Приклад роботи:
#
# Введіть число для обчислення факторіалу: 5
# 5! == 120
# 
# Введіть число для обчислення факторіалу: -5
# Невірний ввод


from functools import reduce


def user_input_factor():
    while True:
        try:
            factorial = int(input('Enter the factorial of number'))
        except Exception:
            print('Incorrect input, Please enter only a positive number')
            continue
        else:
            break
    return factorial


def found_factorial(user_input_factor):
    if user_input_factor < 0:
        print('Неверный ввод')
    else:
        list_n = [i for i in range(1, user_input_factor + 1)]
        result = reduce(lambda x, y: x * y, list_n)
        print(f"!{user_input_factor} = {result}")

found_factorial(user_input_factor())

