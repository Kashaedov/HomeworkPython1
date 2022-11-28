# 2.
# Напишите программудля.проверкиистинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f'Введите значение {xyz[i]}: '))
    return a


def Predicate(x):
    first = not (x[0] or x[1] or x[2])
    second = not x[0] and not x[1] and not x[2]
    result = first == second
    return result


listrez = inputNumbers(3)
if Predicate(listrez) == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
