# legge l'elenco degli studenti iscritti, sotto forma di lista di dizionari

f = open('14BHDOA_2024_shuffled.csv', 'r', encoding='utf=8')

prima_riga = f.readline()  # butta via la prima riga

studenti = []
for line in f:
    campi = line.rstrip('\n').split(',')
    record = {
        'matricola': int(campi[0]),
        'cognome': campi[1],
        'nome': campi[2],
        'cds': campi[6]
    }
    studenti.append(record)
    # print(record)

print(studenti)

f.close()

studenti[7]['matricola']