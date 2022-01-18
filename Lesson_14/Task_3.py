def update_hero(hero=None, power=None, alive=None, speed=None, X=None, Y=None):
    my_dict = {}
    with open("hero.ini", "r", encoding="utf-8") as hero_f:
        while True:
            line = hero_f.readline()[:-1]
            if not line:
                break
            if len(line) == 0:
                continue
            [key, value] = line.split('=')
            my_dict[key] = value
    if hero:
        my_dict["hero"] = hero
    if power:
        my_dict["power"] = power
    if alive:
        my_dict["alive"] = alive
    if speed:
        my_dict["speed"] = speed
    if X:
        my_dict["X"] = X
    if Y:
        my_dict["Y"] = Y

    with open("hero.ini", "w", encoding="utf-8") as hero_f1:
        for key in my_dict:
            hero_f1.write(f"{key}={my_dict[key]}\n")


if __name__ == "__main__":
    update_hero(hero="Hulk", power=800, Y=8.9)
