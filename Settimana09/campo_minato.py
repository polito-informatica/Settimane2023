""" 
Consideriamo il noto gioco del Campo Minato, in cui in una griglia quadrata di NxN caselle sono nascoste M mine.

Il giocatore deve scoprire tutte le caselle che non contengono mine, evitando di scoprire quelle che le contengono.

Il programma deve innanzitutto creare una matrice NxN e posizionare le M mine in posizioni casuali (distinte tra loro). Le mine possono essere rappresentate da un valore Booleano True/False.

In seguito, il programma calcoli una matrice NxN di numeri interi, in cui ciascuna cella contenga il numero di mine presenti nelle 8 celle adiacenti (se esistono).
Si stampi il contenuto di queste due matrici, per verificare la correttezza dei calcoli.

Si permetta poi all'utente di selezionare una casella (inserendone le coordinate di riga e colonna). In funzione del contenuto di tale casella, sono possibili i 
seguenti tre casi:
- casella già selezionata in precedenza: si stampi un messaggio di errore
- casella contenente una mina: si stampi un messaggio di sconfitta (opzionalmente, si termini il programma)
- casella non contentente una mina: si stampi il numero di mine nelle caselle adiacenti

 ..x.   1211
 .x..   1121 
 ....   2210
 x...   0100

 N (int) lato della matrice (campo di gioco)
 M (int) numero di mine seminate

 la posizione delle mine: 
    tabella N righe e N colonne contenente '.' o 'x'
        [ ['.', '.', 'x', '.'], ['.', 'x', '.', '.'], ...... ]
    ** tabella N righe e N colonne contenente False o True
        [[False,False,True,False], [False,True,False,False], ...]
    lista di coppie di coordinate delle mine:
        [ [0,2], [1,1], [3][0] ]
    lista di stringhe contenenti ciascuna una riga di miner
        [ "..x.", ".x..", "....", "x..." ]

 numero di mine adiacenti ad una determinata cella:
    tabella N x N di interi
        [[1,2,1,1],[1,1,2,1],[2,2,1,0],[0,1,0,0]]

"""

from random import randint


def main():
    # leggi N e M
    # N = int(input("Dimensione del campo minato: "))
    # M = int(input("Numero di mine da inserire: "))
    N = 10  # da togliere :)
    M = 15

    # costruisci la matrice NxN contenente M mine
    mine = crea_mine(N, M)
    print_mine(mine)

    # calcolare la matrice delle mine adiacenti
    vicine = calcola_adiacenti(mine)
    print_vicini(vicine)


def crea_mine(N, M):
    """Crea il campo minato sotto forma di tabella di booleani

    Args:
        N (int): lato del campo minato (quadrato di NxN celle)
        M (int): numero di mine da inserire nel campo (deve essere << N²)

    Returns:
        list[list[bool]]: tabella (lista di liste) di N righe ed N colonne. Ciascuna cella contiene un valore booleano
        True (c'è una bomba) o False (nessuna bomba)
    """
    # creo tabella NxN di False
    tab = []
    for i in range(N):
        tab.append([False] * N)

        # riga = []
        # for j in range(N):
        #     riga.append(False)
        # tab.append(riga)

        # tab.append([])
        # for j in range(N):
        #     tab[-1].append(False)

    # metto M mine nella tabella
    for m in range(M):
        r = randint(0, N - 1)
        c = randint(0, N - 1)

        while tab[r][c]:
            r = randint(0, N - 1)
            c = randint(0, N - 1)

        tab[r][c] = True

    return tab


def calcola_adiacenti(mine):
    """Calcola, per ogni casella del campo minato, il numero di mine presenti nelle caselle adiacenti, e restituisce
    una tabella di numeri, con tale conteggio per ogni casella.

    Args:
        mine (list[list[bool]]): campo minato (tabella NxN di booleani)

    Returns:
        list[list[int]]: tabella NxN contenente, per ogni casella [i][j], il numero di bombe nelle 8 caselle adiacenti
    """
    N = len(mine)
    num = []  # numeri di mine vicine

    # costruisco un matrice di NxN zeri ()
    for i in range(N):
        num.append([0] * N)

    for r in range(N):
        for c in range(N):
            num[r][c] = conta(mine, r, c)
    return num


def conta(mine, r, c):
    """Determina quante mie ci sono nelle caselle ADIACENTI a mine[r][c].
    Restituisce un intero tra 0 e 8"""
    N = len(mine)
    tot = 0

    # for i in range (r-1, r+2):  # (righe che devo vedere)
    for i in [r - 1, r, r + 1]:
        for j in [c - 1, c, c + 1]:
            # if i e j sono nell'intervallo 0-N
            # if 0 <= i < N and 0 <= j < N and not(i==r and j==c):
            # if 0 <= i < N and 0 <= j < N and (i!=r or j!=c):
            if 0 <= i < N and 0 <= j < N and (i, j) != (r, c):
                if mine[i][j]:
                    tot = tot + 1
    return tot


def print_mine(mine):
    """Stampa il campo minato in modo esteticamente decente

    Args:
        mine (list[list[bool]]): il campo minato da stampare
    """
    N = len(mine)
    for i in range(N):
        for j in range(N):
            if mine[i][j]:
                print("x", end="")
            else:
                print(".", end="")
        print()


def print_vicini(vicini):
    """Stampa i numeri di adiacenti (utile solo per debug/controllo)

    Args:
        vicini (list[list[int]]): tabella dei numeri di bombe adiacenti
    """
    N = len(vicini)
    for i in range(N):
        for j in range(N):
            print(vicini[i][j], end="")
        print()


main()  # chiamata della funzione principale
