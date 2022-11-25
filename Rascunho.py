lista = ({'idade': 22}, {'idade': 28})
media = list()
for x, y in enumerate(lista):
    media.append(y['idade'])
print(sum(media) / len(media))