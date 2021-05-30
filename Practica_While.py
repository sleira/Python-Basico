edad=int(input("Indroduce la edad por favor: "))

while edad<5 or edad>100:
	print("Haz introducido una edad Incorrectam66. Vuelve a Intentearlo")
	edad=int(input("Indroduce la edad por favor: "))

print("Gracias por colaborar")
print("La edad del aspirante " + str(edad))