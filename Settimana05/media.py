# Inserisci dei numeri reali
# terminando l'inserimento con *
# calcola e stampa la loro media

somma = 0.0
conteggio = 0

letto = ""
while letto != "*":
    letto = input("Numero: ")
    if letto != "*":
        num = float(letto)
        somma = somma + num
        conteggio = conteggio + 1

media = somma / conteggio
print(media)
