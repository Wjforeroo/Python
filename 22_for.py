'''
#Desde 0 hasta 19
for element in range(20):
  """El metodo range proporciona una secuencia de numeros 
  desde 0 hasta el numero que   se le pasa como parametro.
  """
  print(element)

#Desde 1 hasta 20
for element in range(1, 21):
  """El metodo range proporciona una secuencia de numeros 
  desde 0 hasta el numero que   se le pasa como parametro.
  """
  print(element)

my_list = [23, 46, 67, 89, 43]
for element in my_list:
  print(element)

my_tuple = ("nico", "juli", "santi")
for i in my_tuple:
  print(i)
'''

product = {
  "name" : "Camisa",
  "price" : 100,
  "stock" : 89,
}
for key in product:
  print(key,product[key])

for key, value in product.items():
  print(key, value)

#Lista de diccionarios: Formato muy utilizado.
people = [
  {
    "name" : "nico",
    "age" : 34
  },
  {
    "name" : "zule",
    "age" : 45
  },
  {
    "name" : "santi",
    "age" : 4
  }
]
for person in people:
  print(person)
  print("name: ", person["name"])

#for: cuando sepas exactamente cuántas veces quieres que se repita el código o cuando necesites iterar sobre una secuencia de elementos específica, como una lista, tupla, rango u otro objeto iterable.