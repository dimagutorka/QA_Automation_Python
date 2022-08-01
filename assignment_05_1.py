# Завдання: порахуйте кількість літер строки. Строка та літера
#           даються на вхід користувачем. В залежності від кількости
#           виведіть на екран поясненя:
#           строка містить літеру "с" до 10 разів, строка містить літеру
#           "с" більш ніж 10 раз и меньш до 20 разid, строка містить
#           символ "c" більше 20 разів. Проінформуйте користувача якщо
#           введено більше ніж одну літеру (літера має довжину більше 1)
#           або повідомляти якщо такої літери взагалі не знайдено.
#
# Підказка:
# * input() - ввод від користувача
# * len(str) - довжина строки
# * str.count(letter) - підрахунок елементів (літер) letter
# * if - elif - else - для логіки виводу на екран
#
# Приклад:
#
# Введіть текст: Це якийсь рандомний текст
# Введіть літеру: й
# Строка містить літеру "й" до 10 разів.
#
# Введіть текст: аааааааааааааааааааааааа
# Введіть літеру: а
# Строка містить літеру "а" більше 20 разів.

string = input('Enter the string')
letter = input('Enter the letter')

length_string = len(letter)
count_letter_in_str = string.count(letter)

if 1 <= count_letter_in_str < 10 and length_string == 1:
    print(f'String "{string}" contains letter "{letter.upper()}" less than 10 times')
elif 10 <= count_letter_in_str < 20 and length_string == 1:
    print(f'String "{string}" contains letter "{letter.upper()}" more than 10 times and less 20 times')
elif count_letter_in_str > 20 and length_string == 1:
    print(f'String "{string}" contains letter "{letter.upper()}" more than 20 times')
elif length_string >= 2:
    print(f'The length of the letter "{letter.upper()}" more than 2 letter. Enter 1 letter please')
elif not letter.isalpha():
    print("it's not letter. Enter letter, please")
elif letter not in string:
    print(f'Letter "{letter.upper()}" is not contained in string - "{string}"')
else:
    print('Something went wrong')
