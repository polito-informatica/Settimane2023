FILE_POPOLAZIONE = 'worldpop.txt'
FILE_SUPERFICIE = 'worldarea.txt'
FILE_DENSITA = 'world_pop_density.txt'

def leggi_numeri(nome_file):
    nazione = []
    numeri = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for line in f:
            parole = line.split()
            numero = int(parole[-1])
            nome = ' '.join(parole[0:-1])
            nazione.append(nome.strip())
            numeri.append(numero)

    return nazione, numeri

def calcola_densita(popolazione, superficie):
    densita = []

    for i in range(len(popolazione)):
        if superficie[i]!=0:
            d = popolazione[i] / superficie[i]
            densita.append(d)
        else:
            densita.append(-1)  # valore 'sentinella' per indicare l'anomalia
    return densita


def scrivi_densita(nome_file, nazioni, densita):
    with open(nome_file, 'w', encoding='utf-8') as f:
        for i in range(len(nazioni)):
            nome = nazioni[i]
            d = densita[i]
            f.write(f'{nome:40s}\t{d:10.2f}\n')


# PROGRAMMA PRINCIPALE

# leggo il primo file

    # NO: troppo grezzo -- una lista di stringhe (righe intere del file)
    # una lista di stringhe con i nomi delle nazioni
        # nazione[i]
    # una lista di interi con la popolazione
        # popolazione[i]
    # queste liste sono gestite in modo 'parallelo'
    # cioè vanno accedute con uguali valori dell'indice
nazione, popolazione = leggi_numeri(FILE_POPOLAZIONE)
# print(nazione)
# print(popolazione)

# leggo il secondo file
    # stessa cosa, costruisco
    # nazione[i], nomi delle nazioni (gli stessi!!)
    # supercifie[i], area delle superfici delle nazioni
nazione, superficie = leggi_numeri(FILE_SUPERFICIE)
# print(superficie)

# calcolo le densità di popolazione
    # calcola una terza lista, di numeri reali:
    # densita[i] = popolazione[i] / superficie[i]
densita = calcola_densita(popolazione, superficie)
# print(densita)


# pos_superficie = 0
# for n_pop in popolazione:
#     # pos_superficie = popolazione.index(n_pop)
#     d = n_pop / superficie[pos_superficie]
#     pos_superficie = pos_superficie+1
#     densita.append(d)
    
# AARRGHHH
# for n_pop in popolazione:
#     for n_sup in superficie:
#         d = n_pop / n_sup
#         densita.append(d)


# creo il file di uscita
    # crea il file e stampa i valori di
    # nazione[i] e densita[i]
scrivi_densita(FILE_DENSITA, nazione, densita)