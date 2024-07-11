name = "William Joseph"
last_name = "Forero Ortega"
age = 27
print(name)
print(last_name)

#Concatenacion de strings
full_name = name+ " " + last_name
print(full_name)
print(name + " " + last_name)

quote = "I'm William"
print(quote)

quote2 = 'She said "Hello"'

#Format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("Version 1: ",template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("Version 2: ", template)

#La mas utilizada
template = f"Hola, mi nombre es {name} {last_name} y tengo {age} años"
print("Version 3: ", template)