#While True

# while True:
#     print("Hello")

#------------------------------------------------------#

# suma=0
# while True:
#     num=int(input("Ingrese un numero para sumar. Use 0 para salir"))
#     if num==0:
#         break
#     suma+=num
#     print(suma)
# print(f"La suma total es {suma} ")    

#------------------------------------------------------#

# #Pida al usuario el limite inferior y superior de un rango
# #Despues genere un numero al azar dentro de ese rango
# #El segundo numero no deber menor que el primero
# #Pero deben darle la oportunidad al usuario de ingresar otro numero

# import random    

# li=int(input("Ingrese el valor menor de su rango :"))
# ls=int(input("Ingrese el valor mayor de su rango :"))

# while ls<=li:
#     ls=int(input("Elija un numero mayor al menor de su rango :")) 

# ramnum=random.randint(li, ls)
# print(ramnum)

#------------------------------------------------------#

# #Adivinar el numero aleatorio de un rango 1-50.

# import random

# AdNum=int(input("¿Cuál es el numero?"))
# ramnum=random.randint(1,50)

# while AdNum!=ramnum:
#     if AdNum>ramnum:
#         print(f"{AdNum} es mayor que el numero")
#         AdNum=int(input("¿Cuál es el numero?"))
#     else:
#         print(f"{AdNum} es menor que el numero")
#         AdNum=int(input("¿Cuál es el numero?"))
# print("¡Adivinaste el número!")

#------------------------------------------------------#

# #Adivinar el numero aleatorio de un rango 1-50. Con límite de intentos.

# import random

# AdNum=int(input("¿Cuál es el numero?"))
# ramnum=random.randint(1,50)
# intentos=5

# while AdNum!=ramnum:
#     intentos-=1
#     if intentos==0:
#         break
#     if AdNum>ramnum:
#         print(f"{AdNum} es mayor que el numero. Te quedan {intentos} intentos")
#         AdNum=int(input("¿Cuál es el numero?"))
#     else:
#         print(f"{AdNum} es menor que el numero. Te quedan {intentos} intentos")
#         AdNum=int(input("¿Cuál es el numero?"))

# if intentos!=0:
#     print("¡Adivinaste el número!")     
# else:
#     print(f"Te has quedado sin intentos. El numero es {ramnum}")

#------------------------------------------------------#

# #Designe dos peleadores solicitando sus nombres.
# #Cada peleador tiene 50 HP, debe mostrar la barra de energía.
# #Las peleas son por turnos, cada turno el peleador ataca entre 3-15.
# #Existe posibilidad de ataque critico del 20%, será el ataque por 2.
# #Gana el que le quita todo el HP al rival.

# import random
# import time

# p1=(input("Ingrese el nombre del primer peleador :"))
# p2=(input("Ingrese el nombre del segundo peleador :"))

# HP1=50
# HP2=50
# turno=random.randint(1,2)

# while HP1>0 and HP2>0:
#     if turno % 2==0:
#         print("Turno de ", p1)
#         atk=random.randint(3,15)
#         crt=random.randint(1,5)
#         if crt==3:
#             atk*2
#             print("Ataque crítico")
#         HP2-=atk
#         time.sleep(1)
#         print(f"Vida de {p2}")
#         print("|"*HP2)
#     else:
#         print("Turno de ", p2)
#         atk=random.randint(3,15)
#         crt=random.randint(1,5)
#         if crt==3:
#             atk*2
#             print("Ataque crítico")
#         HP1-=atk
#         time.sleep(1)
#         print(f"Vida de {p1}")
#         print("|"*HP1)  
#     turno+=1

# if HP1>HP2:
#     print(f"Ha ganado el peleador {p1}")
# else:
#     print(f"Ha ganado el peleador {p2}")

#------------------------------------------------------#

# while True:
#     print('''
#         1.-
#         2.-
#         3.-Salir
#           ''')
#     op=int(input("Seleccione una opción :"))

#     if op==1:
#         print("Opción 1")
#     elif op==2:
#         print("Opción 2")
#     elif op==3:
#         print("Opción salir")    
#         break
#     else:
#         print("Seleccione una opción válida")

#------------------------------------------------------#

#Crear un cajero automático. 
#Tener en cuenta cajas de billetes de 5000, 10000 y 20000.
#Cada caja tiene 30 billetes. 
#Verificar si el monto solicitado está disponible en el cajero.
#Verificar si el monto solicitado es posible por el multiplo de los billetes disponibles.
#Al terminar cada transacción debe mostrar saldo disponible.
#Debe haber 3 usuarios, cada uno con su saldo correspondiente.
#Usar clave secreta para iniciar sesión y segun la clave asociar el saldo disponible.
                                                                             