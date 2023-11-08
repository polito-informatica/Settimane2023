"""
Si scriva un programma che:
- acquisisca da tastiera un numero intero positivo N
- acquisisca da tastiera N frasi (una per riga) composte di più parole
- per ciascuna frase, identifichi i nomi propri in essa presenti 
  (un nome proprio ha la prima lettera maiuscola, e le altre minuscole)
- VARIANTE 1: si stampino tutti i nomi propri incontrati
- VARIANTE 2: si stampi solo il primo nome proprio incontrato su ciascuna riga
"""

# data una stringa contenente una frase, cerchiamo un nome promprio (Xxxxxx)
import string


frase = "oggi Piero è andato a pescare con Antonio"

# se volessimo evitare di trattare come casi particolari il primo carattere e l'ultimo
# carattere della stringa, basterebbe aggiungere dei caratteri "di riempimento" fittizi
# frase = " " + frase + " "

# troviamo le lettere maiuscole nella stringa
for i in range(len(frase)):
    if frase[i].isupper():
        # il carattere 'i' è un possibile inizio di nome maiuscolo
        # print(frase[i], i)
        if (i == 0) or (frase[i - 1].isspace() or frase[i - 1] in string.punctuation):
            # equivalente: if (i==0) or not(frase[i-1].isalpha() or frase[i-1].isdigit()):
            # equivalente: if (i==0) or (not frase[i-1].isalpha() and not frase[i-1].isdigit()):

            # sappiamo che: la lettera maiuscola non è preceduta da altre lettere o numeri
            # dobbiamo verificare che tutti i caratteri successivi (almeno uno)
            # siano minuscoli ed il primo carattere non minuscolo sia tassativamente
            # uno spazio o un simbolo di punteggiatura

            # cerco "in avanti" da i+1 in poi il primo carattere non minuscolo
            j = i + 1
            while j < len(frase) and frase[j].islower():
                j = j + 1
            # verità: j=len(), quindi ho solo trovato minuscole fino in fondo (ok)
            # oppure: frase[j] non è minuscola (ok se spazio/punt, ko se lett/num)
            if j == len(frase) or (frase[j].isspace() or frase[j] in string.punctuation):
                # verità: ho trovato un nome proprio dal carattere i al carattere j-1
                if j > i + 1: # purché sia lunga almeno 2 caratteri...
                    print(frase[i:j])
