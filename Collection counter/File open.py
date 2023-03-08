a = open("Car.py","w")
k = a.write("""
print("Car Detail
        Brand: BMW
        Colour: Black
        Size: 2.5
        CC: 1500")  """)
print(k)
a.close()