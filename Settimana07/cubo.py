# Costruisco una funzione che calcoli il volume di un cubo
# nome: volume_cubo
# argomenti: lato (numero reale, >=0)
# valore restituito: volume (numero reale)
def volume_cubo(lato):
    calcolo = lato * lato * lato
    return calcolo

def stampa_decorato(n):
    print("***", n, "***")
    return

lato1 = 7.0
volume1 = volume_cubo(lato1)
print(volume1)

lato2 = 3.5
volume2 = volume_cubo(lato2)
print(volume2)

stampa_decorato(volume_cubo(2.1))

