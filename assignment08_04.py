# Завдання: написати функцію лінійного пошуку елементу у послідовності.
#           На вхід подається послідовніть (iterable: list, tuple, str)
#           як перший аргумент, та елемент який потрібно знайти у
#           послідовності (другим елементом). Результатом виконання
#           функції буде індекс першого елементу (якщо такий елемент
#           знайдено) чи None (у разі якщо у послідовності відсутній
#           потрібний елемент.
#
#           Послідовність може вводитися користувачем, або рандомною
#           генерацією, або просто використати літеральні послідовності
#           надані безпосередньо у коді (бажано надати приклади з
#           використанням різних типів послідовностей та елементів,
#           пошук літер у строках, чисел у послідовностях чисел, слів
#           у списку слів).
#
#           Лінійний пошук: це перебір елементів послідовності зліва
#           направо, по одному, до тих пір поки не знайдено потрібний
#           елемент, або, якщо такий відсутній, - більше немає елементів
#           у послідовності.
#
# Приклад:
#
#         s = "Hello world"
#         print(linear_search(s, "w"))  # prints: 6
#         print(linear_search(s, "W"))  # prints: None
#         words = ["Hello", "world"]
#         print(linear_search(words, "planet")  # prints: None
#         nums = tuple(range(10))
#         print(nums, 3)  # prints: 4
#


digit = tuple(range(10))
letter = ['a', 'b', 'c', 'd']
word = ['house', 'goat', 'door', 'sky']


def element_search(array, elem_to_find):
	for i, j in enumerate(array):
		if j == elem_to_find:
			return i

	return None


print(element_search(digit, 0))
print(element_search(letter, 'b'))
print(element_search(word, 'door'))
print(element_search(digit, -1))
