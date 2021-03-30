initial_elem = 1
n = int(input("Введите размерность матрицы: "))
a = [[0 for j in range(n)] for i in range(n)]
start_i = 0
start_j = 0
horizontal = n
vertical = n - 1
n_output = n
while n >=0:
    horizontal = n
    vertical = n - 1
    i = start_i
    j = start_j
    # Заполнение верхней строки
    while j < horizontal:
        a[i][j] = initial_elem
        initial_elem += 1
        j += 1
    i += 1
    j -= 1
    # Заполнение правого столбца
    while i < vertical:
        a[i][n - 1] = initial_elem
        initial_elem += 1
        i += 1
    # Заполнение нижней строки
    while j >= start_j:
        if initial_elem <= n_output * n_output:
            a[i][j] = initial_elem
        initial_elem += 1
        j -= 1
    i -= 1
    j +=1
    # Заполнение левого столбца
    while i > start_i:
        a[i][start_j] = initial_elem
        initial_elem += 1
        i -= 1
    start_i = i + 1
    start_j = j + 1
    n = n - 1
# Вывод матрицы
for i in range(n_output):
    for j in range(n_output):
        print(str(a[i][j]).rjust(3, " "), end=' ')
    print()
print()
