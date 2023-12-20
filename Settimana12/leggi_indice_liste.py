# leggere index.txt sotto forma di lista di liste

import operator


def leggi(nomefile):
    indice = []
    f = open(nomefile, 'r', encoding='utf-8')
    for line in f:
        campi = line.rstrip('\n').split(':')
        campi[0] = int(campi[0])
        indice.append(campi)
    f.close()
    return indice

indice = leggi('index.txt')
indice.sort(key=operator.itemgetter(1))
print(indice)
