# Quali sono i nomi più frequenti?

import csv
import operator


ELENCO = "14BHDOA_2024_shuffled.csv"
NUM_RISULTATI = 10


def main():
    studenti = leggi_studenti(ELENCO)
    nomi = [studente["NOME"] for studente in studenti]

    # opzionale: si potrebbero dividere i nomi multipli in più elementi distinti
    # nomi_splittati = []
    # for nome in nomi:
    #     nomi_splittati.extend(nome.split())
    # nomi = nomi_splittati

    # per ogni nome, calcola quante volte compare
    # costruisci un dizionario: chiave = nome(str), valore = numero di occorrenze (int)
    frequenze = dict()
    for nome in nomi:
        frequenze[nome] = frequenze.get(nome, 0) + 1

    # converti dizionario in lista di tuple
    tabella_frequenze = list(frequenze.items())
    # ordina la lista per frequenza descrescente
    tabella_frequenze.sort(key=operator.itemgetter(1), reverse=True)

    stampa_tabella(tabella_frequenze, NUM_RISULTATI)


def leggi_studenti(nome_file):
    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        elenco = list(reader)
    return elenco


def stampa_tabella(tabella_frequenze, num):
    print("Nomi piu frequenti:")
    i = 1
    for nome, numero in tabella_frequenze[:num]:
        print(f"{i:2d}. {nome:20s}: {numero:3d}")
        i += 1


main()
