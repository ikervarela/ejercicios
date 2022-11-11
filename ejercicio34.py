print ("1) Cuadrado")
print ("2) Triangulo")
eleccion=int (input("Ingrese un número"))
if eleccion==1:
    lado= int (input("Ingrese un lado"))
    area= lado*lado
    print (area)
elif eleccion==2:
    base=int(input("Ingrese una base"))
    altura =int(input("Ingrese una altura"))
    area= (base*altura)/2
    print (area)
else:
    print ("Error")