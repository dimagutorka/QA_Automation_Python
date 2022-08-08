"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""

allow_operator = ['+', '*']

left_number = input('Enter the left operand')
right_number = input('Enter the right operand')
operator = input("Select operator ('+', '*')")


def calculator(left_number, operator, right_number):
    if right_number.isdigit():
        right_number = int(right_number)
    if left_number.isdigit():
        left_number = int(left_number)

    if operator not in allow_operator:
        return None

    elif operator == '+':
        return left_number + right_number
    elif operator == '*':
        return left_number * right_number


print(calculator(left_number, operator, right_number))
