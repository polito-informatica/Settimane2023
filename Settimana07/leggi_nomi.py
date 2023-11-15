# Leggi da tastiera 5 nomi

NUM = 5

nomi = []

# for i in range(NUM):
#     nome = input(f'Nome {i+1}: ')
#     # nomi.append(nome)
#     nomi.insert(0, nome)
nomi = ['uno', 'due', 'tre',  'cinque', 'due']  ## DATI FAKE

print("Inserisci 5 nomi separati da virgole")
nomi_stringa = input()
nomi = nomi_stringa.split(',')

print(nomi)

for i in range(len(nomi)):
    nomi[i] = nomi[i].strip()

print(nomi)

# for nome in nomi:
#     nome = nome.strip()

# print(nomi)



# print(nomi)
# stampa l'elenco dei nomi separandoli con una virgola, senza apici né parentesi quadre
# es: uno, due, tre   e NON ['uno', 'due', 'tre']

# for i in range(len(nomi)):
#     nome = nomi[i]

for i, nome in enumerate(nomi):
    # if è l'ultimo:
    if i==len(nomi)-1:
    # if nomi.index(nome) == len(nomi)-1:
    # if nome == nomi[-1]:
        print(f'{nome}', end='')
    else:
        print(f'{nome}, ', end='')
print()


for nome in nomi[:-1]:
    print(f'{nome}, ', end='')
print(f'{nomi[-1]}')

print(', '.join(nomi))

# nuovo = input("Nome nuovo: ")

# if nuovo in nomi:
#     pos = nomi.index(nuovo)
#     print(f'Trovato in posizione {pos}')
# else:
#     print('Non trovato')