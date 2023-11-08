"""
Si stampi una tabella delle prime potenze dei primi numeri interi,
come la seguente:

         1         2         3         4
        x         x         x         x 
      -----------------------------------
         1         1         1         1
         2         4         8        16
         3         9        27        81
         4        16        64       256
         5        25       125       625
         6        36       216      1296
         7        49       343      2401
         8        64       512      4096
         9        81       729      6561
        10       100      1000     10000

        
Il programma deve leggere il numero N (numero di righe) ed il numero M 
(numero di colonne, cioè di potenze) e stampare la tabella corrispondente.
"""

# definisci il numero di righe e di colonne
# righe == basi // colonne == potenze
# N = int(input("Righe: "))
# M = int(input("Colonne: "))
N= 10
M=6
lun = 10

# stampa l'intestazione
# prima riga: gli esponenti
for esponente in range(1,M+1):
  print(f'{esponente:{lun}d}', end='')
print()
# seconda riga: le x
# for esponente in range(1,M+1):
#   print(" "*(lun-2)+"x ", end='')
# print()
print((" "*(lun-2)+"x ")*M)
# terza riga: i trattini
print('-' * (M*lun))


# per ciascuna base da 1 a N
for base in range(1, N+1):
  # stampa una riga con le potenze di quella base
  # print(f"Potenze della base {base}")
  # prendi ciascuno degli esponenti da 1 a M
  for esponente in range(1, M+1):
    # calcola e stampa base**esponente
    potenza = base ** esponente
    # print(f'La base {base} elevata a {esponente} fa {potenza}')
    print(f'{potenza:{lun}d}', end='') # stampa un numero senza andare a capo
  # vai a capo
  print()