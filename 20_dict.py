person = {
  "name" : "Daniela",
  "last_name": "Forero Ortega",
  "langs": ["Python", "Javascript"],
  "age": 26
}
print(person)

person["name"] = "Valeria"#Modificar el valor de la llave name
person["age"] -= 6 #Modificar el valor de la llave age (operando. Restando 6)
person["langs"].append("Java")#Agregar un valor a la llave langs, que es una lista
print(person)

del person["last_name"]#Eliminar una llave y su valor.
person.pop("age")#Eliminar una llave y su valor.
print(person)

print("Items")
print(person.items())#Retorna una lista de tuplas, donde cada tupla es un par de llave y valor.

print("Keys")
print(person.keys())#Retorna una lista de llaves.

print("Values")
print(person.values())#Retorna una lista de valores.