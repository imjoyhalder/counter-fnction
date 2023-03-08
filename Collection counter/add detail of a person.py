from datetime import date
name = input("Name: ")
addres= input("Address: ")
age = input("Age: ")
occupation = input("Enter you Profession: ")
institute = input("Enter your Institution name: ")
da_te = date.today()
a = open("Person details.json","w")
k = a.write(f"""
            Detail Store in {da_te}
            Name : {name}
            Age : {age}
            Adress: {addres}
            Institute name : {institute}
            Profession : {occupation}

                """)
a.close()