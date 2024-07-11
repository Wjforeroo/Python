lives = 3
print(type(lives))
age = 12
budget = 100
temperature = 12.12
print(type(temperature))

lives = 2
print(lives)

lives = 3
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 4500000000000000000.1
print(number)

number_b = 0.0000000000000001
print(number_b)

#Programa que suma 3 presupuestos y calcula el promedio
budget_january = input("¿Cual es tu presupuesto para Enero? ")
budget_february = input("¿Cual es tu presupuesto para Febrero?")
budget_march = input("¿Cual es tu presupuesto para Marzo?")

budget_january = int(budget_january)
budget_february = int(budget_february)
budget_march = int(budget_march)

add_budget = budget_january + budget_february + budget_march
averange_budget = add_budget / 3

print(f"El presupuesto promedio es de: {averange_budget}")


