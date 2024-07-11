name = "William"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("William" + "Forero")
print(10 + 20)
print("William" + "27")

age = 27
print("Mi edad es: " + str(age))
print("Mi edad es: {}".format(str(age)))
print(f"Mi edad es: {age}")

age = input("Escribe tu edad: ")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 años sera {age}")