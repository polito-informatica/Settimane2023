# encoding farfallino: ciao -> cifiafaofo

# obiettivo 1 - elaborare tutti i caratteri della stringa e fermarsi alla fine di essa
# obiettivo 2 - encoding farfallino

frase = input("Inserire una frase: ")

i = 0
fraseTradotta = ""

while i < len(frase):

    carattereCorrente = frase[i]   

    if carattereCorrente in "aeiouAEIOU":

        fraseTradotta = fraseTradotta + carattereCorrente + "f" + carattereCorrente
    
    else:

        fraseTradotta = fraseTradotta + carattereCorrente
    
    i = i+1

print(fraseTradotta)