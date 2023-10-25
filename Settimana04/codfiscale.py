codice = input("Codice fiscale: ").upper()

if (len(codice)== 16 and 
codice[0:6].isalpha() and

codice[6:8].isnumeric() and

codice[8] in "ABCDEHLMPRST" and

codice[9:11].isnumeric() and
(1 <= int(codice[9:11]) <= 31 or
41 <= int(codice[9:11]) <= 71) and

codice[11].isalpha() and
codice[12:15].isnumeric() and

codice[15].isalpha() ):

    print("Il codice fiscale è corretto")
else:
    print("Codice errato")

###-------------------------------------------------###
### E se volessi anche stampare il MOTIVO per cui
### il codice è errato (con un messaggio esplicativo?)
###-------------------------------------------------###

### Alternativa 1: catena di 'if' annidate ###

if len(codice)==16:
    if codice[0:6].isalpha():
        if codice[6:8].isnumeric():
            ...
        else:
            print("Anno non è numerico")
    else:
        print("Cognome e nome non alfabetici")
else:
    print("Lunghezza errata")


### Alternativa 2: sequenza di 'if-elif-elif' con condizione INVERTITA ###


if not len(codice)==16:
    print("Lunghezza errata")
elif not codice[0:6].isalpha():
    print("Cognome e nome non alfa")
elif not codice[6:8].isnumeric():
    print("Anno non è numerico")
    ...
else:
    print("Codice ok")

### Alternativa 3: successione 'if' separate, con FLAG per ricordare l'errore ###

nessun_errore = True   # FLAG
if not len(codice)==16:
    print("Lunghezza errata")
    nessun_errore = False
if not codice[0:6].isalpha():
    print("Cognome e nome non alfa")
    nessun_errore = False
if not codice[6:8].isnumeric():
    print("Anno non è numerico")
    nessun_errore = False
    ...
if nessun_errore:
# if nessun_errore == True:
    print("Codice ok")

