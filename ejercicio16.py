lluvia= input ("esta lloviendo?")
lluvia=str.lower ("lloviendo")
if lluvia==("yes"):
    vent=input("esta muy ventoso?")
    vent=str.lower(vent)
    if vent== "si":
     print("esta muy ventoso para un sombrilla")
    else:
     print("tome una sombrilla")
else:
    print ("disfruta tu dia")