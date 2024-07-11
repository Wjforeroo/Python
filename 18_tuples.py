#Las tuplas son inmutables. 
numbers = (1, 2, 3, 5)
strings = ("nico", "zule", "santi", "nico")
print(numbers)
print("Posicipon 0: ", numbers[0])
print("Posicipon 0: ", numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))
print(strings.index("zule"))#Indica la posicion
print(strings.count("nico"))#Cuenta elementos

my_list = list(strings)#Convertir de tupla a lista.
my_list[0] = 'Willy'
my_list.insert(0, "Forero")
print(my_list)
print(type(my_list))

my_list = tuple(my_list)#Convertir de lista a tupla.
print(my_list)
