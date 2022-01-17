with open("task_1.txt", "wt", encoding="utf-8") as a:
    print("Напечатайте построчно любой текст. Для остановки введите пустую "
          "строку")
    while True:
        b = input()
        if b == "":
            break
        a.write(b + "\n")
