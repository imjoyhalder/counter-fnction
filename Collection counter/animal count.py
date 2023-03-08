from asyncore import file_dispatcher
from collections import Counter
from itertools import count
try:
    animal = ["Dog","Cat","Got","Dog","Horse","Alephent","Dog","Dog","Cat","Got","Dog","Horse","Alephent"]
    a = "I am a student . Now I am study at Barisal Polytechnic Institute in CSE deparatment"
    print(Counter(a))
    print(count(a))
except TypeError:
    print("Something went wrong")

a = open("Car.py","w")
k = a.write("""
                print("Car Detail
                Brand: BMW
                Colour: Black
                Size: 2.5
                CC: 1500""")
print(k)
a.close()