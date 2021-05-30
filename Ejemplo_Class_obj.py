class A: # La clasa A no tiene un metodo boolen, siempre devuelve True
   def __init__(self):
      print("Esta es la Clase A")
        
a_obj = A()

if a_obj:
   print("Este es True")
else:
   print('Este es False')
    
class B: # La Clase B tiene un metodo bool, que devolvera el valor falso
   def __init__(self):
      print('Este es la Clase B')
        
   def __bool__(self):
      return False
b_obj = B()
if b_obj:
   print('Este es True')
else:
   print('Este es Falso')

myList = [] # Si no hay elementos devuelve Falso
if myList:
   print('Tiene algunos elementos')
else:
   print('Este no tiene elementos')
    
mySet = (10, 47, 84, 15) # Algunos elementos estan disponibles y devuelve True
if mySet:
   print('Tiene algunos elemento')
else:
   print('Este no tiene elementos')