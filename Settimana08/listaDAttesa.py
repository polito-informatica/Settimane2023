"""
Gestire la lista d'attesa per un locale. Le persone in lista sono identificate con il proprio nome, e non ci sono omonimi. 
Il programma prende in input un'operazione che inserisce l'utente, 
che in questo caso è la persona che gestisce gli ingressi all'evento. 
Le operazioni da gestire sono le seguenti (i nomi delle persone sono a titolo esemplificativo):

P mina -> restituisci la Posizione di mina (se non è presente, segnalalo)
A pippo -> Aggiungi in coda pippo (se è già presente, segnalalo)
R gina -> Rimuovi dalla coda gina (se non è presente, segnalalo)
I john -> Inserisci in testa john (se è già presente, segnalalo) - Da fare a casa: sposta la persona in testa alla coda

Dopo ogni iterazione, il programma restituisce in output la lista d'attesa nel suo stato corrente, con il formato:

1 john
2 gale
3 iram
4 melany
5 pippo

"""

listaDAttesa = ["pippo", "gina", "andrea", "ginevra", "willy", "greta"]

operazione = input("Operazione: ")

while operazione != "":

    operazione = operazione.split()
    azione = operazione[0].upper()
    persona = operazione[1]

    if azione == "A": # Aggiungi in coda

        if persona not in listaDAttesa:
            listaDAttesa.append(persona)
        else: 
            print(persona, " è già presente in coda.")

    elif azione == "R": # Rimuovi dalla coda

        if persona in listaDAttesa:
            listaDAttesa.remove(persona)
        else: 
            print(persona, " non è presente in coda.")

    elif azione == "I": # Inserisci in testa
        
        if persona not in listaDAttesa:
            listaDAttesa.insert(0, persona)
        else: 
            print(persona, " è già presente in coda")
            #print("Si sposta in testa.")
            #listaDAttesa.remove(persona)
            #listaDAttesa.insert(0, persona)
        
    elif azione == "P": # Posizione del partecipante

        if persona in listaDAttesa:
            print(persona+" si trova in posizione "+str(listaDAttesa.index(persona))+", cioè è "+str(listaDAttesa.index(persona)+1)+"^ in coda!\n")
        else: 
            print(persona, " non è presente in coda.")
    else:
        print("Operazione non valida.")


    print("\nLa lista d'attesa è:")
    for i, persona in enumerate(listaDAttesa):
        print(i+1, persona)

    operazione = input("Operazione: ")
