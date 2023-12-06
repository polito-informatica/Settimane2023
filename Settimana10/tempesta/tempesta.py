'''
Risoluzione tema d'esame "Tempesta"

La tempesta viene rappresentata da una matrice (lista di
liste) di numeri interi.
'''

from ctypes import LittleEndianStructure
from pprint import pprint
from tkinter import N


def leggi_tempesta(nome_file):
    f = open(nome_file, 'r', encoding='utf-8')
    righe = f.readlines() # liste di stringhe (riga del file con \n)
    f.close()
    matrice = []
    for riga in righe:
        valori = []
        for carattere in riga.rstrip('\n'):
            if carattere=='_':
                valori.append(0)
            elif carattere.isnumeric():
                valori.append(int(carattere))
            else:
                print("Errore nel formato del file")
        matrice.append(valori)
    return matrice

def ombelico(mappa):
    # calcolo una lista che contiene, per ciascuna riga, la somma degli elementi
    somma_riga = []
    for r in range(len(mappa)):
        somma = sum(mappa[r])
        somma_riga.append(somma)

    max_riga = max(somma_riga)
    pos_max_riga = somma_riga.index(max_riga)

    # calcola il massimo per colonna
    somma_col = []
    for c in range(len(mappa[0])):
        somma = 0
        for r in range(len(mappa)):
            somma = somma + mappa[r][c]
        somma_col.append(somma)
    
    max_col = max(somma_col)
    pos_max_col = somma_col.index(max_col)

    return pos_max_riga,pos_max_col

# def sposta_tempesta(mappa):
#     fai cose per modificare i numeri di mappa[r][c]

def sposta_tempesta(mappa):
    # costruisice una nuova matrice, con i numeri aggiornati,
    # senza modificare mappa[r][c]
    nuova = []
    for riga in mappa:     # 1 4 3 1 1 1 1
        riga2 = list(riga)
        # trova l'elemnto più a destra !=0
        pos = len(riga2)-1
        while riga2[pos]==0 and pos>=0:
            pos = pos -1
        if riga2[pos]!=0:
            riga2[pos] = riga2[pos]-1
        # nuova_riga = []  # 0 1 4 3 1 1 0
        nuova_riga = [0] + riga2[:-1]
        nuova.append(nuova_riga)
    return nuova

mappa = leggi_tempesta('mappa.txt')
pprint(mappa)
r, c = ombelico(mappa)
print(f"L'ombelico è in posizione {r},{c} e vale {mappa[r][c]}")
for _ in range(10): # not tempesta_esaurita(mappa):
#    sposta_tempesta(mappa)
    nuova = sposta_tempesta(mappa)
    mappa = nuova
    #stampa_tempesta(mappa)
    print(mappa)