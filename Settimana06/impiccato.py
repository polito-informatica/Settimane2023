# l'utente inserisce una parola segreta 
# un altro utente prova a indovinare, per 10 tentativi, una lettera alla volta, la parola segreta 
# se l'ha già provata brucia un tentativo
# se non è presente nel segreto, usa un tentativo ma non svela alcuna lettera
# se è presente nel segreto, usa un tentativo e svela la lettera in tutte le posizioni in cui è presente
# a ogni iterazione, il programma restituisce in output una stringa che riporta la lettera iniziale
# e quella finale del segreto, e un numero di "_" pari ai caratteri centrali della parola
# "segreto" -> "s_____o"
# ad ogni lettera indovinata, il programma la mostra nelle posizioni in cui si trova
# "s_____o" -> "se__e_o" (se si indovina la "e")
# il gioco finisce quando il segreto è completamente svelato (vittoria) o quando si superano i 10 tentativi (sconfitta)

segreto = input("Inserire parola segreta: ").lower()
parola = segreto[0] + "_"*len(segreto[1:-1]) + segreto[-1]

tentativi = 0

lettereProvate = ""

print(parola)

while parola != segreto and tentativi < 10:

    lettera = input("Inserire nuova lettera: ").lower()

    if lettera in lettereProvate:

        print("Lettera già provata!")
        tentativi = tentativi + 1

    else:
        
        #consideriamo solo la parte segreta della parola,
        #escludendo quindi la prima e l'ultima lettera
        if lettera in segreto[1:-1]:

            i = 0
            nuovaParola= ""

            while i < len(segreto):

                if lettera == segreto[i]:

                    
                    nuovaParola = nuovaParola + segreto[i]
                else:
                    
                    nuovaParola = nuovaParola + parola[i]
                
                i = i+1
            
            tentativi = tentativi + 1
            parola = nuovaParola
        
        else:
            
            print("La lettera ", lettera, " non è nel segreto!")
            tentativi = tentativi + 1
        
        lettereProvate = lettereProvate + lettera
    print(parola)
    
if parola == segreto:
    print("Hai vinto!")
else:
    print("Ritenta la prossima volta!")

