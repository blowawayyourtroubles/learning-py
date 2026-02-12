# Objetivo: Mad Lib simple
# Resultado esperado: "Había una vez un DRAGÓN llamado PEDRO que comía PIZZA"

# Tu plan:
# 1. Pedir un animal
# 2. Pedir un nombre
# 3. Pedir una comida
# 4. Imprimir la historia completa

# Tu código:



animal_name = input("Insert an animal name: ").upper()
name = input("Insert a name: ").upper()
food = input("Insert a food: ").upper()


story = f"Habia una vez un {animal_name} llamado {name} que comia {food}"

print(story)