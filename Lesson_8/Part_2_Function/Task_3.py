def func3(x, y):
    for num in range(x + 1, y):
        count = 0
        d = 2
        while d < num:
            if num % d == 0:
                count += 1
            d += 1
        if count == 0:
            yield num


for m in func3(1, 100):
    print(m, end=" ")
