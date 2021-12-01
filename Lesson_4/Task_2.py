x = (input('введите натуральное число: '))
if x.isdigit():
    n = 1
    for i in range(1, (int(x)) + 1):
        j = i ** 2
        p = len(str(i))
        j1 = str(j)
        if str(i) == j1[(len(j1)) - int(p):(len(j1)):1]:
            print(f"{i}*{i}={i * i}")
else:
    print("Это не натуральное число")
