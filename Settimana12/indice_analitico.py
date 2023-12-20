# svolgimento esercizio sull'indice analitico proposto sulle slide

def leggi(nomefile):
    indice = dict()
    f = open(nomefile, 'r', encoding='utf-8')
    for line in f:
        campi = line.rstrip('\n').split(':')
        pagina = int(campi[0])
        termine = campi[1]
        if termine in indice:
            indice[termine].add(pagina)
        else:
            indice[termine] = { pagina }
    f.close()
    return indice


def stampa(indice):
    for termine in sorted(indice):
        print(termine+': ', end='')
        pagine = sorted(indice[termine])
        # print(str(pagine)[1:-1])
        pagine_str = [str(p) for p in pagine]
        print( ', '.join(pagine_str))

indice = leggi('index.txt')
stampa(indice)