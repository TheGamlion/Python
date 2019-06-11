import datetime
import random
import math

def age_checker():
    age = input("give me your age: ")
    year = int(datetime.date.today().year) - int(age)
    print(year + 100)


#aufgabe 3 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def less_then_five(arr):
    new_list = []
    for element in a:
        if element < 5:
            new_list.append(element)
    print(new_list)

#aufgabe 4

def zerlegung():
    zahl = int(input("Geb eine Zahl ein: "))
    x = zahl
    while x > 0:
        if (zahl % x ) == 0:
            print(x)
        x -= 1

#aufgabe 4
x = 10
a = []
b = []
while x >0:
    zahl = math.floor(random.random()*10 %10) 
    a.append(zahl)
    zahl = math.floor(random.random()*10 %10) 
    b.append(zahl)
    x -= 1

def gemeinsame_elemente(a,b):
    x =0
    c = []
    for y in a:
        for x in b:
            if x  == y:
                for  z in c:
                    if z == y:
                        break
                    c.append(y) 
    print(c)

print(a)
print(b)
gemeinsame_elemente(a,b)