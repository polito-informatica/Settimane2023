# Intelligenza Demenziale

Dopo il successo di ChatGPT, un ricercatore vuole sviluppare un nuovo algoritmo di intelligenza artificiale, che sia in grado di scrivere delle opere letterarie come la Divina Commedia o i Promessi Sposi.

A tal fine, il ricercatore dispone di un file di testo contenente il testo integrale delle opere letterarie. Il programma deve leggere il testo di una di tali opere, ed apprendere le "frequenze dei 2-lemmi" presenti nel testo, ossia la frequenza con cui compaiono tutte le possibili coppie di parole **consecutive**.
Nell'elaborare i testi, si consideri il testo come completamente minuscolo, e si trattino tutti i simboli di punteggiatura come se fossero degli spazi (*1).

*Ad esempio, ne "I Promessi Sposi", la coppia di lemmi "`si può`" compare 65 volte, la coppia "`la parentela`" compare 3 volte, la coppia "`riflessione dubitativa`" 1 sola volta, e così via.*

Una volta calcolate le frequenze delle coppie consecutive di lemmi, il programma deve generare un testo "verosimile" con le seguenti regole:

 1.    l'utente deve inserire una qualsiasi parola. Se questa parola non compare nel testo, essa viene sostituita dal programma con una parola casuale tra quelle presenti nel testo
 2.   partendo dalla parola del punto 1, il programma identifica la parola successiva, considerando tutte le coppie di lemmi che iniziano con la prima parola, e scegliendo una parola a caso tra le 5 più frequenti (*2).
 3.   ripetere il passo 2, partendo da quest'ultima parola trovata, fino ad ottenere una frase di lunghezza casuale tra 5 e 50 parole.
 4.   ripetere dal punto 1, finché l'utente non inserisce una riga vuota.


### NOTE:

  -  (*1) i simboli di punteggiatura sono definiti dalla costante `string.punctuation`
  -  (*2) nel testo dei Promessi Sposi, alla parola "don" segue "abbondio" per 233 volte, "rodrigo" 157 volte, "ferrante" 24 volte, "gonzalo" 20 volte, "filippo" 3 volte, "pietro" 2 volte, e così via. Il programma sceglierà casualmente uno dei primi 5 nomi, tra quelli con maggior frequenza. Nel caso in cui ci siano meno di 5 successori, si scelga casualmente tra quelli presenti. Nel caso in cui vi siano molti successori con la stessa frequenza, si scelga arbitrariamente.

### Esempio


Se il programma viene addestrato con il testo `promessisposi.txt`, esso potrà presentare le seguenti interazioni (essendoci un fattore casuale, i testi saranno ogni volta diversi):

    Parola: lago
    giaceva consolatevi gli disse renzo si può dir di quel momento e con le parole non è una voce che 
    Parola: don
    rodrigo il cardinale e non si trovava nel suo paese la mano in un po meglio che non si fosse stata
    in fretta la mano al padre molto più a cui la sua strada di nuovo in una mano al padre guardiano
    Parola: don
    abbondio e non era un uomo da quel che si fermò ad essa non ci si fosse una certa distanza a cui
    la mano in un gran parte di più di non so quel che si 
    Parola: ramo
    dalbero né con la mano in quella parte a far qualche tempo che la cosa è qui non si può far le donne e di più in fretta a un 
    Parola: ramo
    dalbero né anche di quel tempo che si fermò su quel momento si può esser veduto che si mise la quale si può far di non so anchio che non ci sia 
    Parola:



### Sviluppi successivi (opzionali)

Chi volesse potrà divertirsi ad arricchire il programma con le seguenti modifiche, elencate in ordine di difficoltà crescente:

 -   con un fattore casuale imprevedibile (ad esempio con la probabilità del 2%), al punto 2 si scelga una parola completamente casuale tra quelle presenti nel testo, anziché quella predetta
 -   anziché scegliere tra le 5 parole successive più frequenti (con egual probabilità tra di loro), scegliere tra *tutte* le parole successive, con una probabilità proporzionale alla loro frequenza calcolata
 -   si effettui la previsione tenendo conto anche dei 3-lemmi (sequenza di 3 parole consecutive, di cui bisogna tenere conto della frequenza di apparizione). Qualora esistano dei 3-lemmi che combacino sulle prime 2 parole con il testo generato finora, si scelga la terza parola tra di essi. Altrimenti, si scelga tenendo conto dei 2-lemmi.
 -  si cerchi (con opportune semplificazioni) di ignorare congiunzioni, articoli e preposizioni: la loro presenza non deve influenzare la frequenza delle parole rimanenti (ad esempio "lago di como" deve essere interpretato come la coppia "lago como", ignorando la preposizione). Però in fase di generazione della frase, occorre nuovamente aggiungere le parole ignorate, di fronte alla parola selezionata, scegliendo anche qui con la frequenza con cui compaionoi nel testo.

### Nota
Il testo da noi generato è effettivamente *demenziale*, ma ci introduce al principio base delle cosiddette intelligenze artificiali generative. Una bellissima spiegazione divulgativa del modo di funzionamento di tali strumenti si trova al sito https://ig.ft.com/generative-ai. Si tratta di una combinazione di algoritmi sofisticati (talvolta geniali), tanta statistica, enormi matrici di numeri, e potenza di calcolo a dismisura.

