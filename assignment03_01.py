from math import sqrt

Px = int(input("Введіть Px: "))
Py = int(input("Введіть Py: "))
Cx = int(input("Введіть Сx: "))
Cy = int(input("Введіть Су: "))
r1 = int(input("Введіть r1: "))
r2 = int(input("Введіть r2: "))

L = sqrt((Px - Cx) ** 2 + (Py - Cy) ** 2)

result = "не належить"
if r1 < L < r2:
    result = "належить"

print(f"Координата ({Px}, {Py}) {result} кільцю за центром у ({Cx}, {Cy}) та радіусами r1 = {r1}, r2 = {r2}")
print(float(L))
