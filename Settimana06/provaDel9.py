
# obiettivo 1 - sommare tutte le cifre di un numero tra loro
# 2356 -> 16

# obiettivo 2 - continuare a farlo fintanto che il risultato non abbia una sola cifra
# 16 -> 7

numero = input("Inserire un numero: ")

while int(numero) > 9:

    i = 0
    somma = 0

    while i < len(numero):

        cifraCorrente = numero[i]

        somma = somma + int(cifraCorrente)

        i = i + 1

    numero = str(somma)

print(numero)