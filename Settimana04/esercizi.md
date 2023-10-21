# Esercizi su confronti, stringhe e condizionali

## Secondo grado

Si scriva un programma per risolvere una qualsiasi equazione di secondo grado, del tipo _ax²_ + _bx_ + _c_ = 0.

Il programma deve segnalare tutte le condizioni particolari (ad esempio nel caso in cui _a_, _b_, e/o _c_ siano nulli) e stampare le soluzioni reali, ove esistono.

## Codice Fiscale

Il codice fiscale italiano ha un formato predefinito:

- tre lettere per il cognome (solitamente consonanti)
- tre lettere per il nome (solitamente consonanti)
- due cifre per l'anno di nascita (00-99)
- una lettera per il mese di nascita (Gennaio A, Febbraio B, Marzo C, Aprile D, Maggio E, Giugno H, Luglio L, Agosto M, Settembre P, Ottobre R, Novembre S, Dicembre T)
- due cifre per il giorno di nascita (01-31 per uomini, 41-71 per donne)
- quattro caratteri (una lettera e tre cifre) per il luogo di nascita
- un carattere di controllo (una lettera)

Scrivere un programma che acquisisca da tastiera un codice fiscale e dica se è formattato correttamente, rispetto alle specifiche dei punti precedenti.

Nota: sarebbe carino anche verificare che il carattere di controllo sia corretto... lo potremo fare solo quando conosceremo i cicli, e con tanta pazienza implementando i passaggi descritti nella pagina di Wikipedia.

Fonte: https://it.wikipedia.org/wiki/Codice_fiscale

## Gender-free

Il cosiddetto linguaggio inclusivo prevede che non si debba usare il genere maschile, ma che si debbano indicare entrambi i generi. Ad esempio, non si dice "ragazzo", ma "ragazzo o ragazza"; analogamente non "ragazzi" ma "ragazzi e ragazze".

Scrivere un programma che legga una sola parola, e sulla base della lettera finale:
- se termina per 'o' (maschile singolare), stampi la parola, e la sua versione femminile (che finisce per 'a')
- se termina per 'i' (maschile plurale), stampi la parola, e la sua versione femminile (che finisce per 'e')
- altrimenti, stampi la parola stessa.

## Y2K

Prima dell'anno 2000, vi era la brutta abitudine di indicare gli anni utilizzando solamente le ultime due cifre (ad esempio, 80 anziché 1980).

Scrivere un programma che legga da un utente il suo anno di nascita (che potrà essere espresso su 2 cifre o su 4 cifre (il programma deve accettare entrambe le forme), e che potrà essere del ventesimo o ventunesimo secolo), e si cerchi di determinare l'età della persona.

Ad esempio, "20" indicherà il 2020 (la persona ha 3 anni, non 103). Oppure "30" indicherà il 1930, perché il 2030 non è ancora arrivato.