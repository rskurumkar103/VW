tons_to_kg = lambda t: t * 1000
kg_to_g = lambda kg: kg * 1000
g_to_mg = lambda g: g * 1000
mg_to_lbs = lambda mg: mg * 0.00000220462

tons = float(input("Enter weight in tons: "))

kg = tons_to_kg(tons)
g = kg_to_g(kg)
mg = g_to_mg(g)
lbs = mg_to_lbs(mg)

print(f"{kg} kg")
print(f"{g} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")
