# Esercizio proposto

*Argomenti richiesti: stringhe, condizionali, confronti*

## Obiettivo

Si realizzi un programma Python che determini il vincitore di una mano di carte al gioco della **Briscola**.

In particolare, il programma riceve:

- l'informazione sul seme di briscola
- la prima carta giocata
- la seconda carta giocata

e deve visualizzari in uscita il messaggio "Vince la prima carta" oppure "Vince la seconda carta"

## Formato dell'input

L'informazione sul seme di briscola è rappresentata da una stringa di un carattere, che contiene la lettera maiuscola rappresentativa del seme. 
I valori possibili sono `'C'` (Cuori), `'Q'` (Quadri), `'F'` (Fiori), `'P'` (Picche). Si assuma che il valore inserito sia sempre corretto.

L'informazione sulla carta giocata è rappresentata tramite una stringa di due caratteri, di cui il primo carattere indichi il valore della carta, ed il secondo indichi il seme (codificato come sopra). Il valore della carta è rappresentato da un singolo carattere, compreso tra i seguenti: `A 2 3 4 5 6 7 J Q K`. Ad esempio, la stringa `"3F"` rappresenta il 3 di Fiori, mentre `"KC"` il re di Cuori.

### Esempio di esecuzione del programma

    Inserisci il seme: C
    Inserisci la prima carta: 2F
    Inserisci la seconda carta: 3P

    La carta vincente è: 2F

## Regole del gioco

Il valore delle carte è il seguente:
- 2, 4, 5, 6, 7 valgono 0 punti, e differiscono solo perché la carta con valore maggiore vince sulla carta con valore minore (esempio: un 4 vince su un 2, anche se entrambe valgono 0 punti)
- le figure J, Q, K valgono rispettivamente 2, 3, 4 punti
- la carta 3 vale 10 punti
- l'asso A vale 11 punti

Secondo le regole del gioco, la carta vincente si determina nel seguente modo:
- una carta con il seme di briscola vince sempre su una carta di seme diverso
- tra due carte con lo stesso seme, vince quella di valore maggiore
- tra carte di seme diverso, vince sempre la prima (a meno che la seconda non sia di briscola).


## Esempi

Assumiamo che il seme di briscola sia `C` (cuori).

| Carta 1 | Carta 2 | Risultato | 
|---------|---------|-----------|
| 6F      | JF      | vince JF  |
| 6F      | JP      | vince 6F  |
| 6F      | 2C      | vince 2C  |
| 2C      | AP      | vince 2C  |
| JC      | 3C      | vince 3C  |