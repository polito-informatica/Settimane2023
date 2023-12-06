'''
Apri il file testo.txt

Finché il file non è finito:
    Leggi la prossima riga dal file
    Separa la riga nelle parole componenti
    Per ciascuna parola trovata:
        Scrivi la parola sul file di uscita


Leggi tutto il file di ingresso (in una lunga stringa,
 in una lista di stringhe, ...)
Elabora la lista di stringhe, separando le parole
(costruisci una lista in cui c'è una sola parola
per posizione)
Scrivi il file di uscita
'''

f_in = open('testo.txt', 'r', encoding='utf-8')
f_out = open('testo2.txt', 'w', encoding='utf-8')

for riga in f_in:
    parole = riga.rstrip('\n').split()
    for parola in parole:
        parola_pulita = parola.strip('.,;:!()')
        f_out.write(f'{parola_pulita}\n')

f_in.close()
f_out.close()
