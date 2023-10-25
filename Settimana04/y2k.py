nascita_s = input("In che anno sei nato/a? ")

if len(nascita_s)==4 and nascita_s.isnumeric():
    nascita = int(nascita_s)
    print('Età=', 2023-nascita)
elif len(nascita_s)==2 and nascita_s.isnumeric():
    nascita = int(nascita_s) # numero tra 00 e 99
    if nascita<=23:
        nascita = 2000+nascita
    else:
        nascita = 1900+nascita
    print('Età=', 2023-nascita)
else:
    print('Formato data errato')
    
    
    