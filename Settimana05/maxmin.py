# Inserisci dei numeri reali POSITIVI
# terminando l'inserimento con *
# e stampa il valore massimo inserito

massimo = 0.0

letto = ""
while letto != "*":
    letto = input("Numero: ")
    if letto != "*":
        num = float(letto)
        if num > massimo:
            massimo = num



print(f"Il massimo vale {massimo}")
