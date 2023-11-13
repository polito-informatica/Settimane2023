


def carta_vincente(carta1, carta2, seme_briscola):
    return 1 se vince il primo 
    return 2 se vince il secondo

    return la carta vincente


briscola = input("Seme briscola: ")
carta1 = input("Carta 1: ")

for seme2 in "CQFP":
    for valore2 in "24567JQK3A":
        carta2 = valore2+seme2

        vincente = carta_vincente(carta1, carta2, briscola)
