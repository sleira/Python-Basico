class Personas(object):

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia
		#super(ClassName, self).__init__()
		#self.arg = arg

	def descripcion(self):

		print("El nombre es: ", self.nombre, "tiene", self.edad, "años", "Vive en: ", self.Lugar_residencia)

class Empleado(Personas):
	
	def __init__(self, salario, antiguedad, nom_empl, edad_empl, resic_empl):

		super().__init__(nom_empl, edad_empl, resic_empl)
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ", self.salario, "Tiene trabajando: ", self.antiguedad, "años")

		
Sharon=Empleado(1500, 2, "Sharon", 50, "España")
Sharon.descripcion()
print(isinstance(Sharon, Empleado)) #valida si pertenece a la clase de empleado

Maria=Personas("Maria", 53, "Venezuela")
Maria.descripcion()
print(isinstance(Maria, Personas)) #valida si pertenece a la clase de empleado