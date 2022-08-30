

import random

Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

Lowercase = Uppercase.lower()

digits= "0123456789"

Symbols ="!@#$%^&*()_+=;:,./[]}{|"


Length = int(input("enter the size of the Password: "))

amount=1

answer = int(input("Do you want it to be Readable? \nIf Yes enter 1\nIf No enter 2\nYour answer: "))

if answer==1:
    
    Upper,Lower,number,symbs= True, True, False, False
    all =""
    if Upper :
        all += Uppercase
    if Lower :
        all += Lowercase
    if number :
     all += digits
    if symbs :
      all += Symbols
    for y in range(amount):
        password= "".join(random.sample(all,Length))
        print(password)

elif answer==2:
    
    Upper,Lower,number,symbs= True, True, True, True
    all =""
    if Upper :
        all += Uppercase
    if Lower :
        all += Lowercase
    if number :
     all += digits
    if symbs :
      all += Symbols
    for x in range(amount):
        password= "".join(random.sample(all,Length))
        print(password)
