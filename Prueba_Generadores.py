def generarNumPares(Limite):
	num=1
	
	while num<Limite:
		yield num*2 # Funcion que devuelve 
		num=num+1

devuelvePares=generarNumPares(10)

## for i in devuelvePares: # Aqui podemos imprimir todos
##	print(i)

# Si solo queremos ir imprimiendo los tres primeros valores se haria
print(next(devuelvePares))
print("Aqui podria ir mas codigo")
print(next(devuelvePares))
print("Aqui podria ir mas codigo")
print(next(devuelvePares))



