NOME_FILE = 'voti.txt'

somma_voti_pesati = 0 
somma_crediti = 0

f = open(NOME_FILE, 'r', encoding='utf-8')

for line in f:
    campi = line.rstrip().split()

    nome = campi[0]
    print(nome)
    crediti = int(campi[1])
    voto = int(campi[2])

    somma_voti_pesati = somma_voti_pesati + voto*crediti
    somma_crediti = somma_crediti + crediti

f.close()

media_pesata = somma_voti_pesati / somma_crediti

print(f'La tua media è {media_pesata:.2f}')