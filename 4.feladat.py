#Fej vagy írás

import random

tipp=str(input("Fej vagy írás?: "))

Tlista=["fej", "írás"]

if(tipp==random.choice(Tlista)):
    print("Gratulálok, nyertél!")
else:
    print("Sajnálom, vesztettél. :C ")    