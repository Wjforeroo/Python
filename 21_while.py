#While - Mientras
#Sintaxis
#While: cuando no sepas de antemano cuántas veces necesitas repetir el código y quieres que el bucle se ejecute mientras se cumpla una condición específica.
"""
counter = 0
while counter < 10:
  counter += 1
  #counter = counter + 1
  print(counter)


counter = 0
while counter < 20:
  counter +=1
  if counter == 15:
    break #Romper el ciclo de manera forzada, si se cumple la condicion del if.
  print(counter)
"""

counter = 0
while counter < 20:
  counter += 1
  if counter < 15:
    continue
  """Cuando se cumple la condicion del if, 
  continue: se salta el print o toda la logica que esta por debajo 
  y continua con el siguiente iteracion del while.
  En este caso,
  Solo imprime los numeros del 15 al 20.
  """
  print(counter)