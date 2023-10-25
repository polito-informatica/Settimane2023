parola = input("Immetti una parola: ")

# ultima = parola[len(parola)-1]
ultima = parola[-1]

# if ultima == 'o' or ultima == 'O':
# if ultima.lower() == 'o':
if ultima == 'o':
# if parola.endswith('o'):
    # femminile = parola[0:len(parola)-1] + 'a'
    femminile = parola[:-1] + 'a'

    # NO perché le stringhe sono immutabili
    # femminile = parola
    # femminile[-1] = 'a'

    # NO NO NO femminile = parola.replace('o', 'a')

    print(f"{parola} e {femminile}")

elif ultima == 'i':
    femminile = parola[0:len(parola)-1] + 'e'

    print(f"{parola} e {femminile}")

else:
    print(parola)