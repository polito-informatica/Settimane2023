"""
Dati in ingresso:
- Larghezza totale del muro
- Lato piastrella (ipotesi: piastrelle quadrate, 
  piastrelle bianche abbiano la stessa dimensione delle nere)

Dati in uscita:
- Numero di piastrelle bianche
- Numero di piastrelle nere 
- Spazio da lasciare in ciascun lato

Tutte le misure sono espresse in cm

il numero di piastrelle totali dovrà essere sempre dispari
numero di piastrelle totali = larghezza muro // lato piastrella
(non funziona in generale)

Pensiamo di organizzare il problema in questo modo
N BN BN BN BN
L 2L 2L 2L 2L

Formula corretta:
numero di coppie BN = (larghezza muro - lato piastrella N) // 2L

numero piastrelle bianche = numero di coppie BN
numero piastrelle nere = numero piastrelle bianche + 1
spazio = (larghezza muro - (lato piastrella * numero piastrelle)) / 2
"""

muro = 100
lato = 18
coppie = (muro - lato) // (2 * lato)

bianche = coppie
nere = coppie + 1

spazio = (muro - (lato * (bianche+nere)))/2

print('Dato un muro lungo', muro, 'cm ed una piastrella di lato', lato, 'cm')
print('Dovrò posizionare', bianche, 'piastrelle bianche e', nere, 'nere')
print('e lasciare', spazio, 'cm liberi da ogni lato')

