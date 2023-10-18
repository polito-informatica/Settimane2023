piano = int(input("A che piano vuoi andare? "))

# if piano==13:
#     print("il piano non esiste")
# elif piano<=12:
#     piano_reale = piano
# else:
#     piano_reale = piano-1

# print(f'Devo salire di {piano_reale} piani')


if piano<0 or piano==13:
    print('piano inesistente')
else:
    # normale
    if piano<=12:
        piano_reale = piano
    else:
        piano_reale = piano-1
    print(piano_reale)
    if(piano_reale==0):
        print('sei già qui')

# if piano==13:
#     # anomalo
#     pass  # TODO: gestire l'errore
# else:
#     print('ok')

# if piano==13:
#     print("errore")
