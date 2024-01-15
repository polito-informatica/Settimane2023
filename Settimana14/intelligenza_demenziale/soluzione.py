import operator
import string
import random

def leggi_romanzo(nome_file):
    parole = []
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            riga2 = riga.rstrip('\n').lower()
            for ch in string.punctuation:
                riga2 = riga2.replace(ch, " ")
            campi = riga2.split()
            parole.extend(campi)

    return parole # lista_parole_pulite

def calcola_frequenze(parole):
    frequenze_coppie = dict()
    
    for i in range(len(parole)-1):
        coppia = ( parole[i], parole[i+1] )
        if coppia in frequenze_coppie:
            frequenze_coppie[coppia] += 1
        else:
            frequenze_coppie[coppia] = 1

    return frequenze_coppie

def trova_prossima(corrente, dizionario_frequenze):
    candidati = []  # lista di tuple (parola, freq)
    for coppia in dizionario_frequenze:
        if coppia[0] == corrente:
            candidati.append((coppia[1], dizionario_frequenze[coppia]))

    candidati.sort(key=operator.itemgetter(1), reverse=True)

    if len(candidati)==0:
        return ""

    primi5 = candidati[:5]

    # ci siamo convinti che candidati[] non sarà MAI vuoto
    pos = random.randint(0, len(primi5)-1)
    prossima = primi5[pos]

    # prossima = random.choice(primi5)  # equivalente

    return prossima[0]  # restituisco la parola (str)


def genera_frase(parola_iniziale, dizionario_frequenze):
    
    corrente = parola_iniziale
    print(corrente, end=' ')

    for n in range(random.randint(5, 50)):
        prossima = trova_prossima(corrente, dizionario_frequenze)
        corrente = prossima
        print(prossima, end=' ')

    print()

def main():
    romanzo = leggi_romanzo('promessisposi.txt')
    frequenze_coppie = calcola_frequenze(romanzo)

    parola = input("Parola: ").lower()
    while parola!="":
        if parola not in romanzo:
            parola = random.choice(romanzo)

        genera_frase(parola, frequenze_coppie)
        parola = input("Parola: ").lower()
    
main()