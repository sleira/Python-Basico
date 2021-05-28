# Las tuplas son mas rapidas que una lista al ejecutarse
# ocupa menos espacio en memoria, es obtimizada y da mas rendimiento
# la tupla es con parentencia y la lista con corchete
miTupla=("a", "b", "Sharon", 14, 1,)
miLista1=["1", "2", "3", "4"]
miLista=list(miTupla) #construimos una variable lista igual a mi tupla
print(miTupla[2]) #imprime el elemento que esta en el numero indicado
print(miLista)
miTupla1=tuple(miLista1) # Estamos convirtiendo una Tupla con los mismos valores de la lista 
print(miTupla1) 
print("Juan" in miTupla) # in valida si esta en la tupla Juan
print(miTupla.count(14)) # valida cuantos datos 14 hay en la tupla
print(len(miTupla)) # indica cuantos elementos hay en la tupla
unitariTupla=("Sharon", ) # asi se declara una tupla unitaria es decir solo tiene el valor sharonç
print(unitariTupla)
sinParTupla="Sharon", 12, 23, 4 # se puede declarar sin parentecis
print(sinParTupla)
miTuplaUsa=("Sharon", 12, 23, 1989) # declaramos la tupla
nombre, edad, dia, year=miTuplaUsa # se declaran variables para guardar los campos de la tupla
print(nombre)
print(edad)
print(dia)
print(year)
