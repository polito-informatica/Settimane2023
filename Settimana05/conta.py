# Inserisci dei numeri reali
# terminando l'inserimento con *
# e dimmi quante volte compare il numero 3

tre = 0

letto = ""
while letto != "*":
    letto = input("Numero: ")
    if letto != "*":
        num = float(letto)
        if num == 3.0:
            tre = tre + 1


print(f"Ho visto {tre} tre")
