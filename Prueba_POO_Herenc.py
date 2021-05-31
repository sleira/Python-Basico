class Vehiculos(object):
	
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerado: ", self.acelera, "\nFrenado: ", self.frena)

class Moto(Vehiculos): # Asi hereda de vehiculo
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
			self.enmarcha, "\nAcelerado: ", self.acelera, "\nFrenado: ", self.frena, self.hcaballito)

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if (self.cargado):
			return "La Furgoneta esta Cargada"
		else:
			return "La Frgoneta no esta Cargada"

class VEelectricos(Vehiculos): #Clase independiente
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100
		
	def cargaEnergia(self):
		self.cargando=True

class BicicletasElectrica(VEelectricos, Vehiculos):
	pass



miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFuroneta=Furgoneta("Renault", "Kangoo")
miFuroneta.estado()
print(miFuroneta.carga(True))

miBici=BicicletasElectrica("MarcaBici", "SLR")
