import random
number = random.randrange(1, 101, 1)
# print(number)
guess_number = input("Угадайте число в диапазоне от 1 до 100 ")
counter = 0
while guess_number != number:
    counter += 1
    if guess_number.isdigit() and 0 < int(guess_number) < 101:
        if int(guess_number) == number:
            print(f"Молодец, вы угадали число{number} c {counter} попытки ")
            guess_number = number
        else:
            if int(guess_number) < number:
                guess_number = input("Число меньше, попробуйте еще раз ")
            else:
                guess_number = input("Число больше, попробуйте еще раз ")
    else:
        guess_number = input("Введеное значение не отвечает условию, попробуйте еще раз ")
