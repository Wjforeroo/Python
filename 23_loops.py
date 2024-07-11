matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(matriz[0])#Posición 0 de la lista matriz.
print(matriz[0][1])#Posición 2 de la lista matriz.

for row in matriz:
  print(row)
  for column in row:
    print(column)