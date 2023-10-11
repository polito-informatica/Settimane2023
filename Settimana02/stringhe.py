# ESERCIZIO
# Dato un nome di persona, stamparlo con la prima
# lettera correttamente maiuscola
# es: 'gigi' -> 'Gigi'

nome1 = 'pIeRoUpRipcO'
prima_lettera = nome1[0]
prima_lettera_maiuscola = prima_lettera.upper()

resto = nome1[1:]
resto_minuscolo = resto.lower()

nome2 = prima_lettera_maiuscola+resto_minuscolo
print(nome2)

nome2 = nome1[0].upper() + nome1[1:].lower()
print(nome2)

nome3 = nome1.lower().replace(nome1[0], nome1[0].upper(), 1)
print(nome3)

# ESERCIZIO PROPOSTO
# Data una stringa, sostituire tutte le vocali
# con la vocale successiva. a->e->i->o->u->a
# es. 'gatto' -> 'gettu', 'trucco' -> 'traccu'
# Se possibile, conservare il 'case' delle lettere:
# es. 'Aereo' -> 'Eiriu'

parola = 'cane'

modificata = parola.replace('e', 'i').replace('a', 'e')
# NON SI PUÒ FARE, la replace() non funziona così    .replace('ae', 'ei')

print(modificata)