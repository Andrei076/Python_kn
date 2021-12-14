text = "Кто же вас гонит: судьбы решение? Зависть ли тайная? злоба ль " \
       "открытая? Или на вас тяготит преступление? Или друзей клевета " \
       "ядовитая?"
d = dict()
for i in text.split():
    if d.get(i) is not None:
        d[i] += 1
    else:
        d[i] = 1
m = max(d.values())
for key in sorted(d.keys()):
    if d[key] == m:
        print(key)
        break
