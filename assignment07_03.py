# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
#
# підказка:
#  %= N  # compound assignment


K = int(input('Enter the item will be out '))
N = int(input('Enter the list border'))

if K > N:
    K %= N

a = [i for i in range(1, N) if i % K != 0]
