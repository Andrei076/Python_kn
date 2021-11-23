a = input("Какой сейчас год? ")
if a.isdigit():
    a = int(a)
    if 1900 < a < 1000000:
        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    print(str(a)+" год высокосный")
                else:
                    print(str(a)+" год не высокосный")
            else:
                print(str(a)+" год высокосный")
        else:
            print(str(a)+" год не высокосный")
    else:
        print("Не соответствует требованию")
else:
    print("Не соответствует требованию")
