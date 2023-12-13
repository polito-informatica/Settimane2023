def leggi_numero():
    s = input("Numero: ")
    ok = False
    while not ok:
        try:
            n = int(s)
            ok = True
        except ValueError:
            print(f'Attenzione: {s} non è un numero valido')
            s = input("Numero: ")

    return n

x = leggi_numero()
print(x)