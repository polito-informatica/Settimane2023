import operator


def leggi_menu():
    menu = dict()
    with open("menu.txt", 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            menu[campi[0]] = [campi[1].strip(), float(campi[2]), float(campi[3])]
    return menu

def leggi_ordine(menu):
    ordine = []
    with open('ordine.txt', 'r', encoding='utf-8') as f:
        for riga in f:
            campi = riga.rstrip('\n').split(',')
            campi[1] = int(campi[1])
            altri_campi = menu[campi[0]]
            ordine.append(campi+altri_campi)
    return ordine


menu =leggi_menu()
ordine = leggi_ordine(menu)
ordine.sort(key=operator.itemgetter(4))
print("RICEVUTA")
somma_prezzi = 0.0
somma_iva = 0.0
for voce in ordine:
    print(f'{voce[1]:3d} {voce[2]:30s} {voce[3]*voce[1]:8.2f} IVA {voce[4]:5.2f}%')
    somma_prezzi += voce[3]*voce[1]
    somma_iva += (voce[3]*voce[1]) * voce[4]/100.0 / (1+voce[4]/100.0)
    # prezzo_ivato / (1 + aliquota ) * aliquota

print(f"TOTALE: {somma_prezzi:.2f}")
print(f"Di cui IVA: {somma_iva:.2f}")