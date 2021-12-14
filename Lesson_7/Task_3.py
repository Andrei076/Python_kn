text = input('Введите текст:')
d = {}
for i in text.split():
    if d.get(i) is not None:
        d[i] += 1
    else:
        d[i] = 1
for j, t in d.items():
    print(f'Слово: {j}, Встречается в тексте: {t} раз')

