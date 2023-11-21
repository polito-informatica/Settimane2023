"""
Cinque liste di cantanti del cuore. Si sta creando una playlist per una festa (appena finiti gli esami...)
Si vuole che nella playlist sia presente una canzone per cantante, considerando tutte le preferenze espresse da tutte le persone
alla festa. 
Alcune preferenze sono condivise tra diverse persone, ma dovranno comunque comparire nella playlist una singola volta.
"""

cantanti1 = ["Sting", "JayZ", "Beyonce", "Cosmo"]
cantanti2 = ["Madame", "Cosmo", "Eminem"]
cantanti3 = ["Sting", "JayZ"]
cantanti4 = ["Eminem", "Madame"]
cantanti5 = ["Beyonce", "Nicki"]

# uniamo tutte le liste con una concatenazione
cantanti = cantanti1 + cantanti2 + cantanti3 + cantanti4 + cantanti5
print("Lista di tutti i cantanti: ", cantanti)

# STRATEGIA: aggiungiamo ogni cantante una sola volta ad una nuova lista

# creiamo la nuova lista dove mettere i cantanti in singola copia
cantantiUnici = []

for cantante in cantanti:
    
    #aggiungiamo il cantante corrente solo se non l'abbiamo già aggiunto alla nuova lista
    if cantante not in cantantiUnici:
        cantantiUnici.append(cantante)

# VANTAGGIO: mantiene l'ordine degli elementi nella lista che deriva dalla concatenazione delle liste originali
# SVANTAGGIO: per liste con molti elementi può diventare dispendioso in termini di tempo

print("Lista di cantanti unici: ", cantantiUnici)

