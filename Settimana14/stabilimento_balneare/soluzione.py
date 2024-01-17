def leggi_stabilimento():
    stabilimento = []
    with open('stabilimento.txt', 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            stabilimento.append({
                "ombrelloni": int(campi[0]),
                "prezzo_ombrellone": int(campi[1]),
                "sedie": int(campi[2]),
                "prezzo_sedia": int(campi[3])
            })
    return stabilimento

def cerca_fila(stabil, n_ombrelloni, n_sedie, budget):
    for fila in range(len(stabil)):
        if (stabil[fila]["ombrelloni"]>=n_ombrelloni 
            and stabil[fila]["sedie"]>=n_sedie
            and n_ombrelloni*stabil[fila]["prezzo_ombrellone"]+n_sedie*stabil[fila]["prezzo_sedia"] <= budget):
            return fila
    return -1


### Programma principale

stabil = leggi_stabilimento()

clienti = dict()
incasso = 0.0

with open('ingressi-uscite.txt', 'r', encoding='utf-8') as f:
    for riga in f:
        campi = riga.rstrip('\n').split(',')
        cliente = campi[0]
        if len(campi)==4:
            # entra
            n_ombrelloni = int(campi[1])
            n_sedie = int(campi[2])
            budget = int(campi[3])

            fila = cerca_fila(stabil, n_ombrelloni, n_sedie, budget)
            if fila == -1:
                print(f'Per {cliente} non ci sono file compatibili') 
            else:
                print(f"Il cliente {cliente} è in fila {fila+1}")

                clienti[cliente] = (fila, n_ombrelloni, n_sedie)
                stabil[fila]["ombrelloni"] -= n_ombrelloni
                stabil[fila]["sedie"] -= n_sedie
                incasso += n_ombrelloni*stabil[fila]["prezzo_ombrellone"]+n_sedie*stabil[fila]["prezzo_sedia"]
        else:
            # esce
            print(f'Il cliente {cliente} è uscito')
            (fila, n_ombrelloni, n_sedie) = clienti[cliente]
            stabil[fila]["ombrelloni"] += n_ombrelloni
            stabil[fila]["sedie"] += n_sedie
            clienti.pop(cliente)
    print(f'Incasso della giornata: {incasso:.2f}')
