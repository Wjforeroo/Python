"""
text = "Ella sabe programar en Python"


print("Python" in text)

if "python" in text:
  print("Elegiste bien")


size = len("Amor")#Longitud de la cadena
print(size)

print(text)
print(text.upper())#Cambia el texto a mayusculas
print(text.lower())#Cambia el texto a minusculas
print(text.count("a"))#Cuenta cuantas veces hay un caracter
print(text.swapcase())#Transforma de minuscula a mayuscula y viceversa
print(text.startswith("Ella"))#Verifica si el texto inicia con una palabra
print(text.endswith("Rust"))#Verifica si el texto termina con una palabra
print(text.replace("Python", "Go"))

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize())#Pone el primer caracter en mayuscula
print(text_2.title())#Pone el inicio de cada palabra en mayuscula
print(text_2.isdigit())#Verifica si el texto es un digito
print("398".isdigit())
"""

import random
user_option = input("Piedra, Papel o Tijera: ").lower()
computer_option = random.choice(["piedra", "papel","tijera"])


if user_option == computer_option:
  print("Empate")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("Piedra le gana a tijera")
    print("User es el ganador")
  else:
    print("Piedra gana a papel")
    print("Computer gano")
elif user_option == "papel":
  if computer_option == "piedra":
    print("Papel le gana a Piedra")
    print("User es el ganador")
  else:
    print("Tijera gana a papel")
    print("Computer gano")
elif user_option == "tijera":
  if computer_option == "papel":
    print("Tijera le gana a papel")
    print("User es el ganador")
  else:
    print("Piedra gana a tijera")
    print("Computer gano")