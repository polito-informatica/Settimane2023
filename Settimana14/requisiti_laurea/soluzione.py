import operator

def leggi_esami(nome_file):
    esami = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            if campi[3]!='A' and campi[3]!='R':
                if campi[3]=='30L':
                    campi[3] = 33 
                else:
                    campi[3]=int(campi[3])
                data_dmy = campi[1]
                data_ymd = data_dmy[6:10] + data_dmy[3:5] + data_dmy[0:2]
                campi[1] = data_ymd
                esami.append(campi)
    esami.sort(key=operator.itemgetter(1), reverse=True) # li mette in ordine decresente di data

    # attenzione, ci possono essere coppie (studente, corso) duplicate
    # il primo che incontro nella lista è quello buono, quelli successivi sono da ignorare

    return esami

def leggi_cfu(nome_file):
    cfu = {}
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')

            cfu[campi[0]] = ( int(campi[1]), int(campi[2]) )
    return cfu


def calcola(studente, esami, cfu):
    cfu_obbligatori = 0
    cfu_non_obbligatori = 0
    somma_voti_pesati = 0

    codici = set()

    for esame in esami:
        if esame[0]==studente:

            if esame[2] not in codici:  # quelli successivi sono da ignorare
                cfu_esame, obb = cfu[esame[2]]

                somma_voti_pesati += esame[3] * cfu_esame
        
                if obb==1:
                    cfu_obbligatori += cfu_esame
                else:
                    cfu_non_obbligatori += cfu_esame

                codici.add(esame[2])

    return cfu_obbligatori, cfu_non_obbligatori, somma_voti_pesati / (cfu_obbligatori+cfu_non_obbligatori)

esami = leggi_esami('esami.log')
cfu = leggi_cfu('cfu.dati')
studenti = sorted(set([ esame[0] for esame in esami ]))
for studente in studenti:
    cfu_obb, cfu_non, media = calcola(studente, esami, cfu)
    if (cfu_obb+cfu_non)>=30 and cfu_obb>=10:
        print(f"{studente} è laureabile con {cfu_obb} crediti obbligatori e {cfu_non} non obbligatori. Media={media:.2f}")
    else:    
        print(f"{studente} NON è laureabile con {cfu_obb} crediti obbligatori e {cfu_non} non obbligatori. Media={media:.2f}")