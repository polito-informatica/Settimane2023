from pprint import pprint

N = 5
tab = []

riga = [0]*N
for i in range(N):
    tab.append(list(riga))  # riga.copy()

pprint(tab)
for i in range(N):
    tab[i][i] = 1
pprint(tab)