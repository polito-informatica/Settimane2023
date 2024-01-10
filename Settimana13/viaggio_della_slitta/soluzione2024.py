"""
bambino_corrente = bambino_piu_a_Nord()

while ci sono ancora bambini_rimasti:

    prossimo_bambino = piu_vicino(bambino_corrente, bambini_rimasti)
    consegna_doni(prossimo_bambino)
    tolgo prossimo_bambino dai bambini_rimasti
    bambino_corrente = prossimo_bambino

coordinate = { 'AG': (37.31109,13.576548),
              'IM': (43.941866,7.828637)}

bambini = [
    {'cognome': 'Potter',
    'nome': 'Harry',
    'regalo': 'Bacchetta',
    'provincia': 'VE'},
]

def piu_vicino(bambino_corrente, bambini_rimasti, coordinate):
    distanza_min = 9999999
    for bambino in bambini_rimasti:
        if distanza_province(bambino_corrente['provincia'], bambino['provincia']) < distanza_min:
            distanza_min = distanza_province(bambino_corrente['provincia'], bambino['provincia'])
            bambino_scelto = bambino
    return bambino_scelto
"""


import math


def leggi_bambini(nome_file):
    f = open(nome_file, "r", encoding="utf-8")
    bambini = []
    f.readline()
    for line in f:
        campi = line.rstrip("\n").split(",")
        bambini.append(
            {
                "cognome": campi[0],
                "nome": campi[1],
                "regalo": campi[2],
                "provincia": campi[3],
            }
        )
    f.close()
    return bambini


def leggi_coordinate(nome_file):
    f = open(nome_file, "r", encoding="utf-8")
    coordinate = dict()
    f.readline()
    for line in f:
        campi = line.rstrip("\n").split(",")
        coordinate[campi[4]] = (float(campi[5]), float(campi[6]))
    f.close()
    return coordinate


def bambino_piu_a_nord(elenco_bambini, coordinate):
    indice_bambino = -1
    latitudine_max = -90
    for i in range(len(elenco_bambini)):
        if coordinate[elenco_bambini[i]["provincia"]][0] > latitudine_max:
            indice_bambino = i
            latitudine_max = coordinate[elenco_bambini[i]["provincia"]][0]
    return indice_bambino


def bambino_piu_vicino(provincia_bambino_corrente, elenco_bambini, coordinate):
    distanza_min = 50000  # km
    indice_bambino = -1
    for i in range(len(elenco_bambini)):
        distanza = calcola_distanza(
            provincia_bambino_corrente, elenco_bambini[i]["provincia"], coordinate
        )
        if distanza < distanza_min:
            distanza_min = distanza
            indice_bambino = i
    return indice_bambino


def calcola_distanza(provinciaA, provinciaB, coordinate):
    latA = coordinate[provinciaA][0] * math.pi / 180.0
    lonA = coordinate[provinciaA][1] * math.pi / 180.0
    latB = coordinate[provinciaB][0] * math.pi / 180.0
    lonB = coordinate[provinciaB][1] * math.pi / 180.0

    delta_lat = latB - latA
    delta_lon = lonB - lonA

    h = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(latA) * math.cos(latB) * math.sin(delta_lon / 2) ** 2
    )

    distanza = 2 * 6371.0 * math.asin(math.sqrt(h))
    return distanza

def main():
    bambini = leggi_bambini("bambini.csv")
    coordinate = leggi_coordinate("province.csv")

    bambino_corrente = bambino_piu_a_nord(bambini, coordinate)  # 7
    provincia_bambino_corrente = bambini[bambino_corrente]["provincia"]

    # print("regalo a ", bambino_corrente, provincia_bambino_corrente)
    print(f'Regalo {bambini[bambino_corrente]["regalo"]} a {bambini[bambino_corrente]["cognome"]} {bambini[bambino_corrente]["nome"]} ({bambini[bambino_corrente]["provincia"]})')

    bambini_rimanenti = list(bambini)
    bambini_rimanenti.pop(bambino_corrente)

    while bambini_rimanenti:
        prossimo = bambino_piu_vicino(
            provincia_bambino_corrente, bambini_rimanenti, coordinate
        )
        provincia_bambino_corrente = bambini_rimanenti[prossimo]["provincia"]
        # print("regalo a", prossimo, provincia_bambino_corrente)
        print(f'Regalo {bambini_rimanenti[prossimo]["regalo"]} a {bambini_rimanenti[prossimo]["cognome"]} {bambini_rimanenti[prossimo]["nome"]} ({bambini_rimanenti[prossimo]["provincia"]})')

        bambini_rimanenti.pop(prossimo)


main()
