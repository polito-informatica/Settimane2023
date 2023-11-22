# rimuovere da una lista di stringhe tutte le stringhe di lunghezza < 4 

nomi = ["Abcde", "Fgh", "xx", "Jklmn", "Op", "Qrst"]

# i=0
# while i < len(nomi):
#     if len(nomi[i])<4:
#         # cancellalo
#         nomi.pop(i) 
#     else:
#         i = i + 1

# for i in range(len(nomi)-1, -1, -1):
#     if len(nomi[i])<4:
#         nomi.pop(i)

# 11o comandamento (sulle liste): non si modifica la lista su cui stiamo iterando

# nomi2 = []
# for i in range(len(nomi)):
#     if len(nomi[i])>=4:
#         nomi2.append(nomi[i])
# nomi = nomi2

nomi = [ nome for nome in nomi if len(nome)>=4 ]


print(nomi)