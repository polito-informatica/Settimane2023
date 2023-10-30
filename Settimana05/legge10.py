# leggere una sequenza di numeri.
# Il programma interrompa la lettura quando ha letto 10 numeri
# oppure quando legge il numero 0

'''
i = 0
n = 44
while (i < 10) and (n != 0):
    n = int(input(f"Inserisci il numero {i+1}: "))
    print("Hai inserito", n)
    if n == 0:
        print("Devo uscire dal ciclo")
    i = i + 1
'''

'''
i = 0
# prima iterazione
n = int(input(f"Inserisci il numero {i+1}: "))
print("Hai inserito", n)
i = i + 1
# iterazioni da 2 a 10
while (i < 10) and (n != 0):
    n = int(input(f"Inserisci il numero {i+1}: "))
    print("Hai inserito", n)
    if n == 0:
        print("Devo uscire dal ciclo")
    i = i + 1
'''


i = 0
n = int(input(f"Inserisci il numero {i+1}: "))
while (i < 10) and (n != 0):
    print("Hai inserito", n)
    i = i + 1
    n = int(input(f"Inserisci il numero {i+1}: "))
    if n == 0:
        print("Devo uscire dal ciclo")


i = 0
continua = True
while (i < 10) and continua:
    n = int(input(f"Inserisci il numero {i+1}: "))
    print("Hai inserito", n)
    if n == 0:
        print("Devo uscire dal ciclo")
        continua = False
    i = i + 1

i = 0
esci = False
while (i < 10) and not esci:
    n = int(input(f"Inserisci il numero {i+1}: "))
    print("Hai inserito", n)
    if n == 0:
        print("Devo uscire dal ciclo")
        esci = True
    i = i + 1
