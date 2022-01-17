class PasswordError(Exception):
    def __init__(self, value):
        self.b = value

    def __str__(self):
        return self.b


def my_password():
    a = input("Введите пароль (Правильный: 123d): ")
    my_pass = '123d'
    try:
        if a != my_pass:
            raise PasswordError("Неправильный пароль")
    except PasswordError as err:
        print(err)


my_password()
