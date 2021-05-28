miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid", "Reino Unido":"londres"}
print(miDiccionario["Francia"]) # imprime la clave de Francia que es Paris
print(miDiccionario["España"])
print(miDiccionario) # imprimetodo el diccionario
miDiccionario["Italia"]="Roma" # se le asigna un nuevo valor al diccionario
print(miDiccionario)
del miDiccionario["Reino Unido"] # elimina un elemento del diccionario
print(miDiccionario)
miDiccionario1={"Venezuela":"Caracas", 23:"Jordan", "Moscateros":3} # Podemos tener un diccionario con diferentes tipos de clava
print(miDiccionario1)
miTupla=("España", "Italia", "Venezuela", "Argentina") # Se crea la tupla que seria las claves del diccionario
miDiccionario2={miTupla[0]:"Madrid", miTupla[1]:"Roma", miTupla[2]:"Caracas", miTupla[3]:"Buenos Aires"}
print(miDiccionario2)
print(miDiccionario2["Italia"])
####
miDiccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1994, 1997]}
print(miDiccionario3["Anillos"])
print(miDiccionario3.keys()) # imprime las claves del diccionario
print(len(miDiccionario3)) # imprime la longitud
print(miDiccionario3.values()) # imprime los valores del diccionario