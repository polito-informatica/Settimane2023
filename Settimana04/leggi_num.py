# Legge dall'utente un numero tra 1 e 10
# e continua a chiederlo finché non viene inserito correttamente

n = int(input("Numero: "))

while n<1 or n>10:
    print("Errore, riprova")
    n = int(input("Numero: "))



# tutto il resto del programma che usa 'n'
print(n)