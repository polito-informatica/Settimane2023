# legge l'elenco degli studenti iscritti, sotto forma di lista di dizionari
# utilizzando l'oggetto csvDictReader

import csv

f = open('14BHDOA_2024_shuffled.csv', 'r', encoding='utf=8', newline='')

reader = csv.DictReader(f) # , fieldnames= ['matricola', 'cognome', 'nome', .....metterli tutti]

studenti = []
for record in reader:
    studenti.append(record)
    print(record)

# print(studenti)

f.close()

studenti[7]['matricola']