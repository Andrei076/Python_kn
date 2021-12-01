x = (input('Введите строку: '))
y = (input('Введите символ: '))
n = 0
for i in range(1, (len(x))):
    if x[i] == y:
        n += 1
        print(f"{n} совпадение на позиции {i}")
print(f"Всего совпадений {n}")

# a = input(" Введите строку ")
# b = input("Введите символ")
# n=0
# for i in range(0,len(a)):
#     if a[i]==b:
#         n+=1
# if n>0:
#     print(f"Найдено {n} символа {b}")
# else:
#     print("Такого символа в строке нет")

