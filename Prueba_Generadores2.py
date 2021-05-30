# Cuando colocamos un asteriscos dentro del argumento indica recibe numero indeterminado de argumentos
def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		#yield elemento # devuelve las ciudades
		#for subElemento in elemento: devuelve los suElemento 
		yield from elemento

ciudades_devueltas=devuelveCiudades("Madrid", "Bilbao", "Valencia", "Barcelona")

# Si queremos solo imprimir las dos primeras
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
