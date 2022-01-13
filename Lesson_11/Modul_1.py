import random

M = input("Введите количество срок: ")
if M.isdigit() and int(M) > 0:
    M = int(M)
else:
    print("Вы ввели неправильно")
    exit(2)
N = input("Введите количество столбцов: ")
if N.isdigit() and int(N) > 0:
    N = int(N)
else:
    print("Вы ввели неправильно")
    exit(2)
matrix = [[random.randrange(1, 50) for y in range(N)] for x in range(M)]
MN = []


def rro(matrix1, n, m):
    summa = 0
    for y in range(m):
        for x in range(n):
            summa += matrix1[y][x]
        matrix1[y].append(summa)
        summa = 0


def cco(mn1, matrix1, n, m):
    summa = 0
    for y in range(n):
        for x in range(m):
            summa += matrix1[x][y]
        mn1.append(summa)
        summa = 0


def ausgeben(matrix1, m, n):
    for y in range(m):
        for x in range(n):
            print("%3d" % matrix1[y][x], end=' ')
        print(' ', end=' |')
        print(matrix1[y][n])
    print()
    for z in MN:
        print("%3d" % z, end=' ')


if __name__ == "__main__":
    rro(matrix, N, M)
    cco(MN, matrix, N, M)
    ausgeben(matrix, M, N)
