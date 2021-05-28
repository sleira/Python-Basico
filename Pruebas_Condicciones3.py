salario_presidente = int(input("Introducir el salario presidente: "))
print("salario presidente: " + str(salario_presidente))
salario_director = int(input("Introducir el salario director: "))
print("Salario director: " + str(salario_director))
salario_jefe_area = int(input("Introducir el salario Jefe Area: "))
print("salario Jefe Area: " + str(salario_jefe_area))
salario_adm = int(input("Introducir el salario administrativo: "))
print("salario administrativo: " + str(salario_adm))
if salario_adm<salario_jefe_area<salario_director<salario_presidente:
	print("Salarios Correctos")
else:
	print("Salarios Incorrectos")