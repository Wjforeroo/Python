if True:
  print("Deberia ejecutarse")
if False:
  print("Nunca se ejecuta")
  
'''
pet = input("¿Cual es tu mascota favorita?")
if pet == "Perro":
  print("Genial tienes buen gusto")
elif pet == "Gato":
  print("Espero tengas suerte")
elif pet == "Pez":
  print("Eres lo maximo")
else:
  print("No tienes ninguna mascota interesante")
'''

'''
stock = int(input("Digita el stock: "))
if stock >= 100 and stock <= 1000:
  print("El estock es correcto")
else:
  print("El stock es incorrecto")
  '''

#Proyecto: Crea un programa que evalue si un numero es par o impar
number = input("Ingrese un numero: ")

if number.isdigit():
  number = int(number)
  if number % 2 == 0:
    print("El numero es par")
  elif number % 2 != 0:
    print("El numero es impar")
else:
  print("El valor ingresado no es un numero")


  
        

  
