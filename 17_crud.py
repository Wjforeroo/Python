#CRUD Create, Read, Update & Delete
#Create#####################################################################
numbers = [1, 2, 3, 4, 5]
#Read#######################################################################
print(numbers[:])
#Update#####################################################################
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'Hola')#Inserta (Posicion, Elemento)
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)
index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

#Delete#####################################################################
new_list.remove("todo 1")
print(new_list)

new_list.pop()#ELimina el ultimo elemento, puede recibir parametretro. 
print(new_list)
new_list.pop(0)
print(new_list)

new_list.reverse()#Invierte toda la lista. 
print(new_list)

number_a = [1, 4, 6, 3]
number_a.sort()#Ordena la lista. 
print(number_a)

strings = ["a","z","m","b"]
strings.sort()
print(strings)

#El metodo sort(), no funciona si la lista contiene diferentes tipos de datos.

