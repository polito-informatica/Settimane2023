""" 
Construire una funzione che riceva come parametri una lista di 
stringhe ed un valore soglia, e RESTIUISCA una NUOVA lista che
contiene gli stessi elementi di quella di partenza, tranne quelli
più brevi del valore soglia.
La funzione NON modifica la lista di partenza
"""

def rimuovi(parole, soglia):

    parole2 = list(parole) # lavoro MODIFICANDO una copia
    # così non modifico la lista originaria
    for i in range(len(parole2)-1, -1, -1):
        if len(parole2[i])<soglia:
            parole2.pop(i)

    return parole2


nomi = ["Abcde", "Fgh", "xx", "Jklmn", "Op", "Qrst"]

print(nomi)
nomi2 = rimuovi(nomi, 4)
print(nomi2)