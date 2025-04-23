#Explicación y uso de while

# #Clave con intentos infinitos
# clave=3344
# password=int(input("Ingrese su password :"))

# while clave!=password:
#     print("Error, clave inválida")
#     password=int(input("Ingrese su password :"))

# print("Bienvenido al sistema")    

#------------------------------------------------------#    

#Clave con solo 3 intentos

clave=3344
password=int(input("Ingrese su password :"))
intentos=1

while clave!=password and intentos <=3:
    print("Error, clave inválida")
    intentos+=1
    password=int(input("Ingrese su password :"))

if intentos>=3:
    print("No tiene más intentos")
else:    
    print("Bienvenido al sistema")    
