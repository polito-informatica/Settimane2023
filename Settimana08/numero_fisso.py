""" 
Sia dato un numero di 4 cifre qualsiasi, purché le cifre non
siano tutte uguali tra di loro. (es. 3812)

Ripetere le seguenti operazioni:
- mettere in ordine decrescente le cifre (es. 8321)
- mettere in ordine crescente le cifre (es. 1238)
- calcolare la differenza tra questi due valori (es.8321-1238=7083)
- ripetere il procedimento usando questo nuovo numero

Verificare che questa procedura prima poi arriva ad un numero
terminale (che non cambia più), che è sempre lo stesso.
"""

def leggi_numero():
    # TODO: controlla la correttezza del numero ed evntualmente chiederlo più volte
    n = int(input('Numero: '))
    return n

def calcola_step(n):
    nd = cifre_decrescenti(n)
    nc = cifre_crescenti(n)
    return nd-nc

def cifre_decrescenti(n):
    """Dato un numero intero n compreso tra 0000 e 9999 (non tutte le cifre sono uguali),
    calcola e restituisce un numero intero costituito dalle stesse cifre, messe in ordine
    decresente.
    Es: 37 -> 7300
    """
    n_s = str(n)
    n_s = ( "0000"+n_s )[-4:]
    n_l = list(n_s)
    n_l.sort(reverse=True)
    n_s2 = ''.join(n_l)
    return int(n_s2)

def cifre_crescenti(n):
    n_s = str(n)
    n_s = ( "0000"+n_s )[-4:]
    n_l = list(n_s)
    n_l.sort(reverse=False)
    n_s2 = ''.join(n_l)
    return int(n_s2)



def main():
    n = leggi_numero()

    old_n = 0
    while n != old_n:
        old_n = n
        n = calcola_step(n)
        print(n)

main()
        
# print(cifre_decrescenti(1234))
# print(cifre_decrescenti(8261))
# print(cifre_decrescenti(16))