# num=int(input("Ingrese un numero"))

# if num % 2==0:
#     print("El número es par")
# else:
#     print("El numero es impar")

#------------------------------------------------------#

# #Pida la cantidad de numeros e identifique si es par o impar

# cant=int(input("Ingrese la cantidad de numeros "))

# for i in range(cant):
#     print("Ingrese el numero ")
#     num=int(input())
    
#     if num % 2==0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")    

#------------------------------------------------------#

#Pedir la cantidad de votantes y luego pedir el voto

Mentiroso=0
Corrupto=0
total1=0
total2=0

CantVo=int(input("Ingrese la cantidad de votantes "))

for i in range(CantVo):
    print("¿Por quién va a votar?")
    print("1.-Mentiroso")
    print("2.-Corrupto")
    vot=int(input())
    
    if vot==1:
        print("Su voto es a Mentiroso")
        total1=total1+1
    elif vot==2:
        print("Su voto es Corrupto")
        total2=total2+1
    else:
        print("Elija una opción válida. (1,2)")        

if total1>total2:
    print("El ganador es Mentiroso, con", total1, "votos.")
elif total2>total1:
    print("El ganador es Corrupto, con", total2, "votos.")    
else:
    print("Es un empate")    