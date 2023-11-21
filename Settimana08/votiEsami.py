"""
Siamo alla fine dell'anno accademico, e vorremmo sapere la media dei voti ricevuti per tutti gli esami sostenuti.
Immaginiamo di aver sostenuto 10 esami, tutti con lo stesso numero di crediti. 

Se volessimo eliminare i tre voti più bassi per calcolare la media?
"""

# questa è la lista dei voti ricevuti per ciascun esame
voti = [30, 23, 19, 29, 30, 28, 18, 20, 21, 26]

# STRATEGIA 1 - riomuoviamo i tre voti più bassi con min()
# min() trova il valore più basso - dobbiamo farlo iterativamente

# nuova lista
# per creare una copia della lista originale, dobbiamo usare list()
# remove() toglie un elemento da una lista sulla base del suo valore 
votiAlti = list(voti)
for i in range(3):
    votiAlti.remove(min(votiAlti))

# STRATEGIA 2 - sort() + slicing
# ordiniamo la lista e prendiamo tutti gli elementi tranne gli ultimi tre
# nuova lista (con list()!)

# in alternativa, sorted() crea una nuova lista ordinata, senza modificare la lista di partenza
# votiAlti2=sorted(voti)
votiAlti2 = list(voti)
votiAlti2.sort()
votiAlti2=votiAlti2[3:]

# STRATEGIA 3: sort() + pop() + for loop, che rimuove un elemento da una data posizione della lista
# in alternativa, sorted() crea una nuova lista ordinata, senza modificare la lista di partenza
#votiAlti2=sorted(voti)
votiAlti3 = list(voti)
votiAlti3.sort()

for i in range(3):
    votiAlti3.pop(0)

# volendo calcolare la media, dobbiamo iterare su tutti gli elementi della lista
# possiamo farlo con un ciclo for
# la media si calcola sommando tra loro gli n valori di interesse, e poi dividendo la somma per n
# n lo abbiamo già: altro non è che la lunghezza della lista:
nVoti=len(voti)

# la somma la otteniamo numero per numero, grazie al ciclo for
# inizializziamo la somma a 0
sommaVoti=0
for voto in voti:

    #cominciamo ad esplorare che valore viene associato a voto 
    #a ciascuna iterazione

    #print(voto)
    # vediamo che vengono elaborati i valori nella lista
    # nell'ordine in cui sono presentati

    # ad ogni iterazione, aggiorniamo la somma aggiungendo il numero corrente
    sommaVoti+=voto

# oppure usiamo sum()
#sommaVoti=sum(voti)

mediaVoti=sommaVoti/nVoti
print("Media di tutti i voti:", mediaVoti)

# calcoliamo le medie

nVotiAlti=len(votiAlti)

sommaVotiAlti=sum(votiAlti)
mediaVotiAlti=sommaVotiAlti/nVotiAlti
print("Media di tutti i voti meno i tre più bassi (metodo 1):", mediaVotiAlti)

nVotiAlti2=len(votiAlti2)
sommaVotiAlti2=sum(votiAlti2)
mediaVotiAlti2=sommaVotiAlti2/nVotiAlti2
print("Media di tutti i voti meno i tre più bassi (metodo 2):", mediaVotiAlti2)

nVotiAlti3=len(votiAlti3)
sommaVotiAlti3=sum(votiAlti3)
mediaVotiAlti3=sommaVotiAlti3/nVotiAlti3
print("Media di tutti i voti meno i tre più bassi (metodo 3):", mediaVotiAlti3)