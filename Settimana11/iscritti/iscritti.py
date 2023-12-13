'''
Dato l'elenco degli studenti iscritti, presente nel file '14BHDOA_2024_shuffled.csv,
si vogliono creare molti file che contengano l'elenco "parziale" diviso per Corso di Studi.
Ad esempio, il file "ELN1T3.csv" conterrà tutti e soli gli studenti che nel campo "CDS STUDENTE"
hanno il valore "ELN1T3".
Durante la creazione di tali file, si stampi anche il numero di studenti presenti
in ciascuno dei gruppi.
'''

import csv

COLONNA_CDS = 6

def main():
    # leggo interamente il file di ingresso, in una lista (un elemento per studente)
    # di liste (un elemento per ogni campo)
    # nota: il CdS è nella colonna [6]
    # studenti = [
            # ['326815', 'FALCHI', 'NICOLO'.....],
            # ['312191', 'FALDELLA', 'PIETRO FRANCESCO', ....]
    # ]
    try:
        studenti = leggi_studenti('14BHDOA_2024_shuffled.csv')
    except OSError:
        print("Il file non esiste o non si può aprire")
        exit()
        
 
    # cerco quali sono i vari corsi di studio presenti nel file, e li metto
    # in una lista (senza duplicati)
    # elenco_cds = ['INF1T3', 'FIS1T3', ecc]
    elenco_cds = estrai_cds(studenti)

    # per ciascun elemento di elenco_cds
    # apro un file con il nome giusto
    # scrivo nel file tutti gli studenti del CdS corrispondente
    for cds in elenco_cds:
        try:
            c = scrivi_studenti(cds, studenti)
            print(f'Nel corso {cds} ci sono {c} studenti')
        except OSError:
            print(f'Errore nella creazione del file relativo a {cds}')

def leggi_studenti(nome_file):
    f = open(nome_file, 'r', encoding='utf-8', newline='')
    reader = csv.reader(f)
    studenti = []
    next(reader) # salta la riga di intestazione
    for studente in reader:
        studente[0] = int(studente[0])
        studenti.append(studente)
    f.close()
    return studenti

def estrai_cds(studenti):
    elenco = []
    for studente in studenti:
        cds = studente[COLONNA_CDS]
        if cds not in elenco:
            elenco.append(cds)
    return elenco

def scrivi_studenti(cds, studenti):
    c = 0
    nome_file = cds + '.csv'  # f'{cds}.csv'
    f = open(nome_file, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for studente in studenti:
        if studente[COLONNA_CDS]==cds:
            # f.write(f'{studente[0]},{studente[1]},{studente[2]}...\n')

            # f.write(str(studente)+'\n')

            # ATTENZIONE: si modifica la variable del programma
            # principale, e non dovremmo farlo
            # studente[0] = str(studente[0])
            # f.write(','.join(studente)+'\n')

            # studente_str = [str(campo) for campo in studente]
            # f.write(','.join(studente_str)+'\n')

            writer.writerow(studente)
            c = c+1

    f.close()
    return c

main()