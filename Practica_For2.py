# Usar range
valido=False
email=input("Introduce el email: ")
for i in range(5):
	print(f"valor de la variable {i}") # la f indica que podemos concatenar el mensaje con el valor i

for i in range(5,10): # imprimira a partir de i=5 hasta 10
	print(f"valor de la variable {i}")

for i in range(5,50,3):# Imprimira a partir de 5 al 50 de 3 en 3
	print(f"valor de la variable {i}")

# Usar len me devuelve la cantidad de caracteres que tiene un string
for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido==True:
	print("email Correcto")
else:
	print("email Incorrecto")

