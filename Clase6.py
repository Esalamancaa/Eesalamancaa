# #Calcular el puntaje de credito
# #Debe calcular que tanto credito tiene una persona
# #En cierta entidad financiera, deberá considerar
# #Cantidad de ingresos, nivel educacional y nacionalidad
# #Cantidad de ingresos
# #500.000 a 1.000.000 : 300.000
# #1.000.000 a 1.500.000 : 650.000
# #1.500.001 o mas : 1.000.000
# #Nivel educacional
# #Basico : x1, medio : x1.3, superior x1.5
# #Nacionadidad
# #Chilena : +300.000, Extranjero : +0

# cr=0

# print("¿Cuál es su sueldo?")
# sueldo=int(input())

# if sueldo>=500000 and sueldo<=1000000:
#     cr+=300000
# elif sueldo>1000000 and sueldo<=1500000:
#     cr+=650000
# else:
#     cr+=1000000

# print("¿Cuál es su nivel educacional? : 1.-Basico, 2.-Medio, 3.-Superior.")
# ne=int(input())

# if ne==1:
#     cr*=1
# elif ne==2:
#     cr*=1.3
# else:
#     cr*=1.5

# print("¿Usted es de nacionalidad 1.-Chilena, 2.-Extranjera")      
# na=int(input())  

# if na==1:
#     cr+=300000

# print(f"Según lo ingresado, su puntaje de crédito es: {cr}")     
   

# #Pedir al usuario 2 digitos verificando que el segundo sea mayor
# #Genere un numero aleatorio entre esos digitos
# #E imprima la cantidad de veces el simbolo ▄ (alt+220)

# import random

# d1=int(input("Ingrese un digito :"))
# d2=int(input("Ingrese el segundo digito :"))

# while d1>d2:
#     print("El segundo número no puede ser menor al primero.") 
#     d2=int(input("Ingrese el segundo digito :"))

# nr=random.randint(d1,d2)
# print("▄"*nr)


# # Crear un programa que pida la cantidad de ramos
# # Luego suma el promedio de cada materia
# # Basados en su promedio final, aplicar puntaje de beneficios
# # 4.5 y 5: 300, 5.1 y 6.0: 500, 6.1 y 7.0 : 800
# # Agregar puntaje segun carrera
# # Tecnico : +60, Ingenieria: +40, Diplomado: +20

# pb=0

# print("¿cuantos ramos tiene?")
# cr=int(input())

# for i in range(cr):

#     print(f"¿cuantas notas tiene el ramo {i+1}?")
#     notas=int(input())
#     nf=0
#     for j in range(notas):
#         print(f"Ingrese la nota {j+1}")
#         ne=float(input())
#         nf+=ne
#         promedio=nf/notas
#         if promedio>=4.5 and promedio<=5.0:
#             pb+=300
#         elif promedio>=5.1 and promedio<=6.0:
#             pb+=500 
#         else:
#             pb+=800           
#     print(f"Su promedio en este ramo es: {nf/notas}")

# print("¿Su carrera es: 1.-Tecnico, 2.-Ingeniería, 3.-Diplomado")
# op=int(input())

# if op==1:
#     pb+=60
# elif op==2:
#     pb+=40
# else:
#     pb+=20

# print(f"Su puntaje de beneficios es de: {pb}")        


#ProgramaVerProfe

mat=int(input("Ingrese la cantidad de materias: "))

for i in range(mat):
    notaramo=float(input(f"Ingrese la nota del ramo {i+1}"))
    suma+=notaramo
prom=notaramo/mat

if prom>=4.5 and prom<=5.0:
    puntaje=300
    print(f"Su puntaje de beneficios es de {puntaje}")   
elif prom>=5.1 and prom<=6.0:
    puntaje=500
    print(f"Su puntaje de beneficios es de {puntaje}")    
elif prom>=6.1 and prom<=7.0:
    puntaje=800
    print(f"Su puntaje de beneficios es de {puntaje}")     
else:
    print("Las notas son bajas para optar a un beneficio")

car=int(input('''
Ingrese su tipo de grado
1.- Técnico
2.- Ingeniería
3.- Diplomado                                         
              '''))         

if car==1:
    puntaje+=60
elif car==2:
    puntaje+=60    
elif car==3:
    puntaje+=20
else:
    print("Opción inválida")      

print(f"El puntaje de beneficios es {puntaje}")