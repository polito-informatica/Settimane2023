# leggere index.txt sotto forma di lista di dizionari

import operator


def leggi(nomefile):
    indice = []
    f = open(nomefile, 'r', encoding='utf-8')
    for line in f:
        campi = line.rstrip('\n').split(':')
        indice.append({
            'pagina': int(campi[0]),
            'termine': campi[1]
        })
    f.close()
    return indice

indice = leggi('index.txt')
indice.sort(key=operator.itemgetter('termine'))
print(indice)
