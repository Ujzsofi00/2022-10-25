#Reláció kiiratása

szam1=float(input("Kérem az egyik számot: "))
szam2=float(input("Kérem a másik számot: "))

if(szam1>szam2):
    print(szam1,">", szam2)
elif(szam1==szam2):
    print(szam1,"=", szam2)    
else:
    print(szam2,">",szam1)

