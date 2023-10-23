# Costanti
SEMI = "CQFP"
VALORI = "24567JQK3A"

# Acquisisco i dati
seme_briscola = input("Seme di briscola: ").upper()
carta1 = input("Carta 1: ").upper()
carta2 = input("Carta 2: ").upper()

# Controlla la validità dei dati

# if not(len(seme_briscola)==1 and seme_briscola in "CQFP"):
if len(seme_briscola)!=1  or  seme_briscola not in SEMI:
    print("Seme errato")
    exit()

if len(carta1)!=2 or len(carta2)!=2:
    print("Formato carte errato")
    exit()

if carta1 == carta2:
    print("Le carte devono essere diverse")
    exit()

# Estraggo info utili
seme1 = carta1[1]
seme2 = carta2[1]
valore1 = carta1[0]  # '4'
valore2 = carta2[0]  # 'K'

if seme1 not in SEMI or seme2 not in SEMI:
    print("Seme carte errato")
    exit()

if valore1 not in VALORI or valore2 not in VALORI:
    print("Valore carte errato")
    exit()



# if valore1<valore2:  234567AJKQ

# if valore1=='A':
#     punti1 = 10
# elif valore1=='3':
#     punti1 = 9
# elif valore1=='K':
#     punti1 = 8
# elif valore1=='Q':
#     punti1 = 7
# elif valore1=='J':
#     punti1 = 6
# elif valore1=='7':
#     punti1 = 5
# elif valore1=='6':
#     punti1 = 4
# elif valore1=='5':
#     punti1 = 3
# elif valore1=='4':
#     punti1 = 2
# elif valore1=='2':
#     punti1 = 1

punti1 = VALORI.find(valore1)
punti2 = VALORI.find(valore2)

# Determino carta vincente

if seme1==seme2:
    # semi uguali, briscola o non briscola è lo stesso
    if punti1>punti2:
        print("Vince", carta1)
    else:
        print("Vince", carta2)
else:
    # semi sono diversi
    if seme1 == seme_briscola:
        print("Vince", carta1)
    elif seme2 == seme_briscola:
        print("Vince", carta2)
    else:
        print("Vince", carta1)

    # # alternativa furba
    # if seme2 == seme_briscola:
    #     print("Vince", carta2)
    # else:
    #     # semi diversi, la prima può essere briscola o no, vince comunque
    #     print("Vince", carta1)

# if seme1==seme2 and punti1>punti2:
#     print("Vince", carta1)
# elif seme1==seme2 and punti1<punti2:
#     ...
#     # eccetera 