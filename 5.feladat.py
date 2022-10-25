#Listás feladat

import random
'''
n=int(input("Add meg hány darab eleme legyen a listádnak: "))

lista=random.sample(range(-100,100),n)
print=(lista)
'''

n=int(input("Add meg hány darab eleme legyen a listádnak: "))

randomlist=[]

R=random.randint(-100,100,n)

for R in range(-100,100):
    if(R<0):
        print("Negatív számok: ",R)   
    
