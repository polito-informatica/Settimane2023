from random import randint


piles=[]
total=0

while total < 45:

    current_pile=randint(1, 45 - total)
    piles.append(current_pile)

    total+=current_pile

print("Initial Piles: ", piles, end=" ")
print()

iter=0
while piles!=[1,2,3,4,5,6,7,8,9]:

    iter+=1

    newPiles=[]
    for p in piles:
        newPiles.append(p-1)
    newPiles.append(len(piles))

    while 0 in newPiles:
        newPiles.remove(0)

    newPiles.sort()
    print("Nuove pile: ", newPiles, "Somma carte: ", sum(newPiles))
    print("Iter: ", iter)
    piles=newPiles

