miLista=["a", "b", "c","d","e","f"]
miLista2=["Enrique", "Sharon"]
miLista4=["1", "2"]*3 # multiplica la linea por 3

print(miLista[:])
print(miLista[0])
print(miLista[-2])
print(miLista[0:3]) #imprime desde el 0 al 2
print(miLista[:3]) # toma que esta el 0
print(miLista[2:]) # imprime desde el 2 hasta el final
miLista.append("Prueba") #append agrega siempre al final
print(miLista[:])
miLista.insert(2, "pruebaI") # con el insert podemos agrehar en la posicion indicada
print(miLista[:])
miLista.extend(["Maria", "Jose", "Carlos"]) # extend concatena dos lista
print(miLista[:])
print(miLista.index("a")) # me devuelve el indice donde esta "a" en la lista
print("pepe" in miLista) #in devuelve si un valor esta en la lista con False o True
miLista.remove("Prueba") # remove elimina un elemento de la lista
print(miLista[:])
miLista.pop() # elimina el ultimo elemento de la lista
print(miLista[:])
miLista3=miLista+miLista2 #une las dos lista en la otra variable 
print(miLista3[:])
print(miLista4)

