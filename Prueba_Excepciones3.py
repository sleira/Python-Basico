def evaluaEdad(edad):
	if edad<0:
		raise ZeroDivisionError("No se permiten edades negativas")
	if edad<20:
		return "Eres muy Joven"
	elif edad<40:
		return "Eres Joven"
	elif edad<65:
		return "Eres Maduro"
	elif edad<100:
		return "Cuidate......"

print(evaluaEdad(50))