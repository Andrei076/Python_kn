a = input("Какой сейчас год? ")
if a.isdigit():
    a = int(a)
    if 1900 < a < 1000000:
        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    print(str(a)+" год высокостный")
                else:
                    print(str(a)+" год невысокстный")
            else:
                print(str(a)+" год высокостный")
        else:
            print(str(a)+" год невысокостный")
    else:
        print("Не соответствует требованию")
else:
    print("Не соответствует требованию")
