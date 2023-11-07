'''
Partendo dal programma 'briscola' sviluppato nella Settimana 04, si verifichi la correttezza del suo funzionamento
in modo esaustivo.

L'utente inserisce da tastiera il seme di briscola (C, Q, F, P) ed una delle due carte (es. 3F, KP).

Il programma genera automaticamente *tutte le carte possibili* del mazzo (esclusa quella inserita), e per ciascuna di esse, 
dice l'esito della mano se venisse giocata quella carta per seconda.

Esempio:

Seme di briscola: C
Prima carta: 3Q

Seconda carta:
AC: vince 
2C: vince 
3C: vince 
...
KC: vince 
AQ: vince 
2Q: perde
    (nota: 3Q non c'è)
4Q: perde
...
JQ: perde
QQ: perde
KQ: perde
AF: perde
...
...


Opzionale: ripetere l'esercizio dove la carta inserita dall'utente è da considerarsi la seconda carta
giocata (e quella generata esaustivamente la prima giocata).
'''