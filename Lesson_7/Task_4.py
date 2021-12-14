text = "Кто же вас гонит: судьбы решение? " \
       "Зависть ли тайная? злоба ли " \
       "открытая? Или на вас тяготит преступление? " \
       "Или вас Или друзей клевета ядовитая?"
d = dict()
for i in reversed(text.split()):
    if d.get(i) is not None:
        d[i] += 1
    else:
        d[i] = 1
m = max(d.values())
for key in d.keys():
    if d[key] == m:
        print(key)
        break
