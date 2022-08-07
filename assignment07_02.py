# Згенерувати, за допомогою list comprehension,
# квадратну диагональну матрицю завданої розмірності (N)
# N - запитати у користувача
#
# Приклад:
# N = 4
#
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
# підказка: j+1 if i = j else 0
#

# N = int(input('Enter the size of the matrix'))


def building_matrix():
    N = int(input('Enter matrix size: '))
    a = [[j + 1 if i == j else 0 for i in range(N)] for j in range(N)]
    for i in a:
        print(*i)


building_matrix()
