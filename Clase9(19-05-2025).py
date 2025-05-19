#Otros ejercicios de for

# Perros de caza
# Pida al usuario una cantidad de perros
# Muestre cual es la cuota minima de conejos
# Luego consulte cuantos conejos trajo
# Si el perro trajo la cantidad minima, cumplió la cuota
# Sino se queda sin filete
# Mostrar resumen de perros que cumplieron y los que no

# from random import randint

# cant=int(input("Ingrese un numero de perros :"))

# conejos=randint(5,7)
# print(f"La cuota de conejos para esta ocasión es de {conejos}")

# for i in range(cant):
#     print("¿Cuantos conejos casó el perro ", i+1, "?")
#     cconejos=int(input())
#     if cconejos>=conejos:
#         print("El perro ha cumplido la cuota, tendrá un filete como recompensa!")
#     else:
#         print("No ha cumplido la cuota de conejos")    
    
               
#------------------------------------------------------#

# #VerProfe

# import random
# while True:
#     try:
#         cant=int(input("Ingrese un numero de perros :"))

#         cuota=3
#         cumple=0

#         for i in range(cant):
#             con=random.randint(0,5)
#             print(f"El perro {i+1} trajo {con} conejos")
#             if con>=cuota:
#                 print("El perro gana filete")
#                 cumple+=1
#             else:
#                 print("Se queda sin carne de res") 
                
#         print(f"La cantidad de perros que cumplieron la cuota es: {cumple}")        
#         print(f"La cantidad de perros que no cumplieron la cuota es: {cant-cumple}") 

#     except:
#         print("Solo se aceptan numeros enteros")

#------------------------------------------------------#

# ¿Quiere pasar el ramo?
# Pregunte la cantidad de rojos en el curso
# Hay 4 talleres hay en el semestre
# Por cada taller asistido obtiene 0.3 decimas
# Si el alumno tiene más de 1 punto, tienen la bendición del profesor
# Sino, no se le puede ayudar
# Ingrese la nota final y sume las decimas acumuladas.
# Muestre si aprueba o reprueba

# while True:
#     try:
#         crojos=int(input("¿Cuantos rojos tiene en el curso? :"))
#         total=0
#         for i in range(crojos):
#             print(f"Ingrese el rojo {i+1}. (Con numeros decimales)")
#             notas=float(input())
#             total+=notas

#         print("Ha habido 4 talleres de repaso durante el semestre,")
#         ctalleres=int(input("¿A cuantos talleres ha asistido? :"))
#         dtotal=ctalleres*0.3
#         if ctalleres==4:
#             print("Tiene la bendición del profesor")
#         else:
#             print("Tuvo que haber asistido a más")

#         nfinal=total+dtotal/crojos

#         if nfinal>=4.0:
#             print("Felicidades, ha aprobado")
#             break
#         else:
#             print("Ha reprobado, haga más esfuerzo para la próxima")
#             break    

#     except ValueError:
#         print("Por favor, utilice numeros enteros para empezar")     

#------------------------------------------------------#

# #VerProfe

# rojos=int(input("Diga la cantidad de rojos :"))  
# talleres=4
# tdecimas=0

# for r in range(rojos):
#     for t in range(talleres):
#         print(f"¿Asistió al taller numero {t+1}? Sí/No")
#         assist=int(input())
#         if assist.lower()=="si":
#             tdecimas+=0.3
#     if tdecimas>=1:
#         print("Tiene la bendición del profe")
#     else:
#         print("Nada más que hacer")
#     nf=float(input("Ingrese su nota final :"))
#     nf+=tdecimas
#     if nf>=4:
#         print("El alumno aprobó")
#     else:
#         print("El alumno reprobó")     
          
#------------------------------------------------------#

#Lavado de autos
#Crear un menú para lavar autos
#1.- Cursar pago del lavado.
#2.- Ver ventas diarias.
#3.- Salir
#El lavado tiene 3 niveles
#1.- Full $15.000, 2.- Standar $10.000 y 3.- Básico $7.000
#Al mostrar las ventas diarias, debe mostrar la cantidad de autos que han ingresado y el monto total recadudado.
#También debe mostrar el monto total pagado.

# import os
# import time

# total=0
# at=0
# while True:
#     print('''
#     Sistema de asistencia del autolavado
#         1.- Cursar pago al cliente
#         2.- Ver ventas diarias
#         3.- Salir
#         ''')
#     op=int(input())
#     os.system('cls')
#     match op:
#         case 1:
#             print('''
#     ¿Qué servicio de autolavado se ha elegido?
#                 1.- Full $15.000
#                 2.- Standard $10.000
#                 3.- Básico $7.000
#                 ''')
#             al=int(input())
#             if al==1:
#                 print("El servicio costará $15.000")
#                 total+=15000
#             if al==2:
#                 print("El servicio costará $10.000")
#                 total+=10000
#             if al==3:
#                 print("El servicio costará $7.000")    
#                 total+=7000
#             at+=1    
#             time.sleep(2)
#             os.system('cls')
#         case 2:
#             if al==1:
#                 mp=15000
#             elif al==2 and al!=1:
#                 mp=10000
#             elif al==3 and al!=1 and al!=2:
#                 mp=7000        
#             print(f'''Se han registrado:
#                   Autos: {at}
#                   Ganancias: ${total}
#                   Mayor pago: ${mp}
#                   ''')        
#             ov=input("Ingrese cualquier tecla para regresar")
#             os.system('cls')
#         case 3:
#             print("Saliendo del sistema...") 
#             break   
#         case _:
#             print("Elija una opción válida")
