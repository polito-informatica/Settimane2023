posti=int(input("inserire n posti:"))

parcheggio=[]
for p in range(posti):
    parcheggio.append(False)

round=0
while False in parcheggio:

    

    longestLength=0
    longestPos=0

    for i in range(len(parcheggio)):

        if not parcheggio[i]:
            length=1
            pos=i+1

            while pos<len(parcheggio) and not parcheggio[pos]:

                length+=1
                pos+=1

            if length > longestLength:
                longestLength=length
                longestPos=i

        parcheggio[longestPos+longestLength//2]=True


    for p in parcheggio:

        if p:
            print("X", end="")
        else:
            print("_", end="")

    round=round+1

    print()