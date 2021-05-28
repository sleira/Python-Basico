class Animal():
	vivo=False
	dormir=False
	ronronea=False
	maullar=False

	def dormido(self):
		self.dormir=True

	def roncando(self):
		self.ronronea=True

	def maullando(self):
		self.maullar=True

	def est_dormido(self):
		if (self.dormir):
			return "zzzzzzzz"
	def est_roncando(self):
		if (self.ronronea):
			return "rrrrrrrrr"
	def est_maullar(self):
		if (self.maullar):
			return "miau"

miGato=Animal()
miGato.dormido()
print(miGato.est_dormido())
miGato.roncando()
print(miGato.est_roncando())
miGato.maullando()
print(miGato.est_maullar())
