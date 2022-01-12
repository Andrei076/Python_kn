import random

M = input("Введите число больше 5: ")
if M.isdigit() and int(M) > 5:
    M = int(M)
    print("До сортировки: ")
else:
    print("Вы ввели неправильно")
matrix = [[random.randrange(1, 50) for y in range(M)] for x in range(M)]
for i in range(len(matrix)):
    for r in range(len(matrix[i])):
        print("%3d" % matrix[i][r], end=' ')
    print()
m = list(map(sum, zip(*matrix)))
for t in range(len(m)):
    print("%3d" % m[t], end=' ')


def sortierung(matrix2, sum2, mm):
    for j in range(mm - 1):
        for c in range(mm - 1 - j):
            if sum2[c] > sum2[c + 1]:
                sum2[c], sum2[c + 1] = sum2[c + 1], sum2[c]
                for n in range(mm):
                    matrix2[n][c], matrix2[n][c + 1] = matrix2[n][c + 1], \
                                                       matrix2[n][c]

    for c in range(mm):
        for j in range(mm - 1):
            for n in range(mm - 1 - j):
                if (c % 2 == 0) and (matrix2[n][c] < matrix2[n + 1][c]):
                    matrix2[n][c], matrix2[n + 1][c] = matrix2[n + 1][c], \
                                                       matrix2[n][c]
                else:
                    if(c % 2 != 0) and (matrix2[n][c] > matrix2[n + 1][c]):
                        matrix2[n][c], matrix2[n + 1][c] = matrix2[n + 1][c], \
                                                       matrix2[n][c]
    return matrix2, sum2


def drucken(matrix_, sum_, m_):
    for n in range(m_):
        for c in range(m_):
            print("%3d" % matrix_[n][c], end=' ')
        print()
    for c in range(m_):
        print("%3d" % sum_[c], end=' ')


sortierung(matrix, m, M)
print("\n""После сортировки: ")
drucken(matrix, m, M)