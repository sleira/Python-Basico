nombreUsuario=input("Introduce tu Nombre de Usuario: ")
print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())
edad=input("Introduce la edad: ")

while (edad.isdigit()==False):
	print("Por Favor, Introduce un valor numerico")

	edad=input("Introduce la edad: ")

if (int(edad)<18):
	print("No pueda pasar")
else:
	print("Si puede pasar")

