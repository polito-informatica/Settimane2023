# Costanti
SEMI = "CQFP"
VALORI = "24567JQK3A"


def carta_vincente(carta1, carta2, seme_briscola):
    """Confronta due carte al gioco di briscola e decide quale delle due sia
    la carta vincente in questa mano

    Args:
        carta1 (str[2]): la prima carta
        carta2 (str[2]): la seconda carta
        seme_briscola (str[1]): il seme di briscola attuale

    Returns:
        int: restituisce 1 se la prima carta è vincente, restituisce 2 se la seconda carta è vincente, restituisce 0 in caso di errori
    """
    # Estraggo info utili
    seme1 = carta1[1]
    seme2 = carta2[1]
    valore1 = carta1[0]  # '4'
    valore2 = carta2[0]  # 'K'

    if seme1 not in SEMI or seme2 not in SEMI:
        return 0
        exit()

    if valore1 not in VALORI or valore2 not in VALORI:
        print("Valore carte errato")
        return 0

    if carta1 == carta2:
        print("Le carte devono essere diverse")
        return 0

    punti1 = VALORI.find(valore1)
    punti2 = VALORI.find(valore2)

    # Determino carta vincente

    if seme1 == seme2:
        # semi uguali, briscola o non briscola è lo stesso
        if punti1 > punti2:
            return 1
        else:
            return 2
    else:
        # semi sono diversi
        if seme1 == seme_briscola:
            return 1
        elif seme2 == seme_briscola:
            return 2
        else:
            return 1


# Acquisisco i dati
seme_briscola = input("Seme di briscola: ").upper()
carta1 = input("Carta 1: ").upper()


for seme2 in "CQFP":
    for valore2 in "24567JQK3A":
        carta2 = valore2 + seme2

        if carta1 != carta2:
            vincente = carta_vincente(carta1, carta2, seme_briscola)
            if vincente == 1:
                print(f"{carta1}-{carta2}: vince {carta1}")
            elif vincente == 2:
                print(f"{carta1}-{carta2}: vince {carta2}")
            else:
                print("errore")
