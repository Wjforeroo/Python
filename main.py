import random

options = ("piedra", "papel", "tijera")
user_win = 0
computer_win = 0
rounds = 1

while True:
  
  print("*" * 50)
  print("ROUND", rounds)
  print(f"🙋User wins: {user_win} , 🤖Computer wins: {computer_win}")
  print("*" * 50)

  user_option = input("Piedra, Papel o Tijera: ")
  user_option = user_option.lower()
  computer_option = random.choice(options)
  
  if user_option in  options:
    print("user_options: ", user_option)
  else:
    print(f"{user_option}, no es una opcion valida")
    continue
    
  print("Computer option: ", computer_option)
  if user_option == computer_option:
    print("Empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra le gana a Tijera")
      print(f"User es el ganador de la ronda: {rounds}")
      user_win += 1
    else:
      print("Papel gana a Piedra")
      print(f"Computer es el ganador de la ronda: {rounds}")
      computer_win += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel le gana a Piedra")
      print(f"User es el ganador de la ronda: {rounds}")
      user_win += 1
    else:
      print("Tijera gana a papel")
      print(f"Computer es el ganador de la ronda: {rounds}")
      computer_win += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera le gana a Papel")
      print(f"User es el ganador de la ronda: {rounds}")
      user_win += 1
    else:
      print("Piedra gana a Tijera")
      print(f"Computer es el ganador de la ronda: {rounds}")
      computer_win += 1

  if computer_win == 2:
    print("🎖️El rotundo ganador es la computadora🎖️")
    break
  if user_win == 2:
    print("El rotundo ganador es el usuario")
    break
    
  rounds += 1