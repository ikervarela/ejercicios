import math
radio = int(input("Ingrese el radio del cilindro"))
profundidad= int (input("Ingrese la profundidad del cilindro"))
area=math.pi*(radio**2)
volumen=area*profundidad
print (round(volumen,3))