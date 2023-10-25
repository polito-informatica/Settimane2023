somma = 10000

INTERESSE = 0.05  # interesse del 5% annuo

# somma1 = somma + somma*INTERESSE
# somma2 = somma1 + somma1*INTERESSE
# somma3 = somma2 + somma2*INTERESSE

conta = 0
while somma<20000 :
    somma_fine_anno = somma + somma*INTERESSE
    print(conta, somma_fine_anno)

    somma = somma_fine_anno
    conta=conta + 1