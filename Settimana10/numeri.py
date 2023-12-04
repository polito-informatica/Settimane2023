# leggere i numeri presenti nel fine dati.txt
# e stamparli in ordine crescente di valore

file = open("dati.txt", "r")

dati = []
# s = file.readline()
# while s!='':
#     # print(s)
#     dati.append(int(s))
#     s = file.readline()

for s in file:
    dati.append(int(s))

file.close()

dati.sort()
print(dati)