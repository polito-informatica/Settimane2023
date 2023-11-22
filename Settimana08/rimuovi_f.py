""" 
Costruire una funzione che riceva come argomento una lista di stringhe,
e cancelli da tale lista gli elemnti più brevi di una certa soglia.
La funzione quindi non ha bisogno di restituire alcun risultato
perché modifica già la lista che ha ricevuto come argomento.
"""

def rimuovi(parole, soglia):
    # 'parole' è un alias alla lista che dobbiamo modificare    
    # for i in range(len(parole)-1, -1, -1):
    #     if len(parole[i])<soglia:
    #         parole.pop(i)

    # print(parole)
    parole[:] = [ p for p in parole if len(p)>=soglia ]
    # print(parole)

nomi = ["Abcde", "Fgh", "xx", "Jklmn", "Op", "Qrst"]

print(nomi)
rimuovi(nomi, 4)
print(nomi)