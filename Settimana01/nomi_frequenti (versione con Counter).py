# Quali sono i nomi più frequenti?

import csv
import collections


ELENCO = "14BHDOA_2024_shuffled.csv"


def main():
    studenti = leggi_studenti(ELENCO)
    nomi = [studente["NOME"] for studente in studenti]

    frequenze = collections.Counter(nomi)

    tabella_frequenze = frequenze.most_common(5)

    stampa_tabella(tabella_frequenze)


def leggi_studenti(nome_file):
    with open(nome_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        elenco = list(reader)
    return elenco


def stampa_tabella(tabella_frequenze):
    print("Nomi piu frequenti:")
    for nome in tabella_frequenze:
        print(f"{nome[0]:20s}: {nome[1]:3d}")


main()
