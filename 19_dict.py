my_dict = {}
print(type(my_dict))

my_dict = {
  "name": "William",
  "last_name": "Forero Ortega",
  "age" : "26"
}

print(my_dict)
print(len(my_dict))
print(my_dict["name"])
print(my_dict["last_name"])
print(my_dict["age"])
print(my_dict.get("name"))
print(my_dict.get("last_name"))
print(my_dict.get("age"))

print(my_dict.get("Joseph"))#Si el valor no existe, devuelve None.
print("Willian" in my_dict)#Si el valor existe, devuelve True.
print("joseph" in my_dict)#Si el valor no existe, devuelve False.

