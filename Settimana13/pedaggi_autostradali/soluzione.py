def leggi_passaggi(nome_file):
    passaggi = dict()
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(';')
            targa = campi[0]
            percorso = [ campi[1], campi[2] ]
            if targa not in passaggi:
                passaggi[targa] = [ percorso ]
            else:
                passaggi[targa].append(percorso)
    return passaggi


def leggi_tratte(nome_file):
    tratte = list()
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(';')
            tratte.append( [campi[0], campi[1], float(campi[2])] )
    return tratte

def calcola_pedaggio(ingresso, uscita, tratte):
    # calcola l'indice della tratta che ha ingresso = ingresso
    pos_in = -1
    for i, tratta in enumerate(tratte):
        if tratta[0]==ingresso:
            pos_in = i
    # calcola l'indice della tratta che ha uscita = uscita
    pos_out = -1
    for i, tratta in enumerate(tratte):
        if tratta[1]==uscita:
            pos_out = i
    # il percorso era di "andata"?
    if pos_in != -1 and pos_out != -1 and pos_out >= pos_in:
        pedaggio = 0.0
        for i in range(pos_in, pos_out+1):
            pedaggio += tratte[i][2]
        return pedaggio, pos_out-pos_in+1
    else:
        # è un viaggio di ritorno, rifai tutto da capo
        pos_in = -1
        for i, tratta in enumerate(tratte):
            if tratta[1]==ingresso:
                pos_in = i
        pos_out = -1
        for i, tratta in enumerate(tratte):
            if tratta[0]==uscita:
                pos_out = i
        # scambio out con in perché sono sicuro che in>=out
        pedaggio = 0.0
        for i in range(pos_out, pos_in+1):
            pedaggio += tratte[i][2]
        return pedaggio, pos_in-pos_out+1


def main():
    passaggi = leggi_passaggi('auto.txt')
    tratte = leggi_tratte('pedaggi.txt')


    # print(calcola_pedaggio('Torino', 'Milano', tratte))
    # print(calcola_pedaggio('Volpiano', 'Santhia', tratte))
    # print(calcola_pedaggio('Santhia', 'Volpiano', tratte))
    # print(calcola_pedaggio('Milano', 'Torino', tratte))
    # print(calcola_pedaggio('Balocco', 'Greggio', tratte))
    # print(calcola_pedaggio('Greggio', 'Balocco', tratte))

      # { 'IF245': [ ['Torino', 'Milano'], ['Rho'], ['Chivasso'] ]}
    pedaggi = []
    for targa in passaggi:  # 'IF245'
        elenco_percorsi = passaggi[targa]   # [ ['Torino', 'Milano'], ['Rho'], ['Chivasso'] ]
        pedaggio_tot = 0
        n_tratte_tot = 0
        for percorso in elenco_percorsi: # ['Torino', 'Milano']
            pedaggio, n_tratte = calcola_pedaggio(percorso[0], percorso[1], tratte)
            pedaggio_tot += pedaggio
            n_tratte_tot += n_tratte
        print(targa, pedaggio_tot, n_tratte_tot, len(elenco_percorsi))
        pedaggi.append((targa, pedaggio_tot))

    pedaggio_max = 0.0
    targa_max = ''
    for i in range(len(pedaggi)):
        if pedaggi[i][1]>pedaggio_max:
            pedaggio_max = pedaggi[i][1]
            targa_max = pedaggi[i][0]

    print(targa_max)

main()