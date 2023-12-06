file_voti = open("voti.txt", "r")

tabella_voti = file_voti.readlines()

for i in range(len(tabella_voti)):
    tabella_voti[i] = tabella_voti[i].strip()

# tabella_voti = [ riga.strip() for riga in tabella_voti ]

# for riga in tabella_voti:
#     riga = riga.strip()


file_voti.close()

print(tabella_voti)

file_punteggi = open("punteggi.txt", "w")

for voto in tabella_voti:
    punteggio = int(voto.split()[2])
    # punteggio = int(voto[2].split())
    # file_punteggi.write(f'{punteggio}\n')
    # print(punteggio, file=file_punteggi)
    file_punteggi.write(str(punteggio)+'\n')

file_punteggi.close()


# se volessi usare writelines
# lista = []
# for voto in tabella_voti:
#     punteggio = int(voto.split()[2])
#     lista.append(f'{punteggio}\n')
# file_punteggi.writelines(lista)