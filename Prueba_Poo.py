# Crae Clase
class Coche(object):
	def __init__(self): # asi se crea el constructor y con los dos __ se esta encapsulando los valore
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 
		self.__enmarcha=False

	# crear el comportamiento se hace un Metodo
	# hace referencia a un objeto que pertenece a la clase
	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos

		if self.__enmarcha:
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "El coche esta en Marcha"
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo. no podemos arracar"
		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene: ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis,
			"y un largo de ", self.__largoChasis)

	def __chequeo_interno(self): # Con los dos guiones bajo lo estamos encapsulado
		print("realizando chequeo interno")

		self.gasolina="Ok"
		self.aceite="Ok"
		self.puertas="cerradas"

		if self.gasolina=="Ok" and self.puertas=="cerradas" and self.aceite=="Ok":
			return True
		else:
			return False

miCoche=Coche() # instancia una clase
print(miCoche.arrancar(True))
miCoche.estado()

print("......A continuacion crearemos el segundo Objeto........")

miCoche2=Coche() # instancia una clase
print(miCoche2.arrancar(False))
miCoche2.estado()







		
