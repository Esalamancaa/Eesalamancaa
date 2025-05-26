import random

def azarN():
    num=random.randint(1,10)
    return num

def arancel():
    print('''
    #       "Ingrese la comuna donde vive"
    #     1.- La Florida 2.-La Pintana 3.- Puente Alto 4.-San Joaquin    
    #     ''')
    comuna=int(input())

    print("¿Cuantas personas viven con usted")
    personas=int(input())

    if comuna==1:
        desc=20
    elif comuna==2:
        desc=30
    elif comuna==3:
        desc=25
    elif comuna==4:
        desc=15
    else:
        print("No es una opción válida, intentelo de nuevo")

    if personas==1:
        desc+=2
    elif personas>=2 and personas <=4:
        desc+=3
    else:
        desc+=4     

    arancel=int(200000-(200000*(desc/100)))
    print(f"El arancel final según los datos ingresados es: {arancel}")
    print(f"El descuento es de : {200000*(desc/100)}")

def menu_tarea():
    while True:
        print('''
                Seleccione una opción
            1.- Numero al azar
            2.- Calcular arancel
            3.- Salir
            ''')
        op=int(input())
        match op:
            case 1:
                azarN()
            case 2:
                arancel()
            case 3:
                break    
            case _:
                print("Opción inválida")

    print(f"El total de su compra es {total}") 

#------------------------------------------------------#

#Crear un menú de carrito con las siguientes opciones
# 1.- Ingresar nombre del usuario
# 2.- Comprar, poner productos para poder comprar
# 3.- Sacar boleta, calcular el precio neto y el precio + IVA. Mostrar totales
# Será mostrado en la boleta con un saludo
# 4.- Salir
#Consideraciones: 
# - Por lo menos 3 productos. 
# - No hay limite de compra. 
# - Se puede salir en cualquier momento. 
# - Los precios de los productos son fijos.

# import os

# def comp():
#     total=0
#     while True:
#         print(f'''
#         {nombre}, ¿Qué desea comprar?
#                 1.- Shampoo $2590
#                 2.- Jabón líquido 1lt $1790
#                 3.- Acondicionador $2290
#                 4.- Salir 
#                 ''')  
#         op=int(input())
#         os.system('cls')
#         match op:
#             case 1:
#                 total+=2590
#                 print("Su subtotal es $", total)
#             case 2:
#                 total+=1790
#                 print("Su subtotal es $", total) 
#             case 3:
#                 total+=2290
#                 print("Su subtotal es $", total)
#             case 4:
#                 break 
#             case _:
#                 print("Opción inválida, intentelo nuevamente")   
            
#     print(f"El total de su compra es ${total}") 
#     print(f"El total de su compra + IVA es ${total*1.19}") 
#     print("Muchas gracias por comprar con nosotros,", nombre)

   
# print("Hola, ingrese su nombre: ")
# nombre=input()
# os.system('cls')

# comp()  

#------------------------------------------------------#

# #Ejemplo de return

# def suma_ret():
#     n1=int(input("Ingrese el primer número :"))
#     n2=int(input("Ingrese el segundo número :"))
#     return n1+n2

# nume=suma_ret()

# for i in range():
#     print("Hola")

#------------------------------------------------------#

# Promedios por cantidad de alumnos 
# 1.- Pedir cantidad de alumnos
# 2.- Pedir cantidad de notas por cada alumno
# 3.- Promediar a cada alumno y mostrar si aprueba o reprueba
# Bonus: Mostrar promedio de todos los alumnos ingresados

nA=int(input("Ingrese el número de alumnos :"))

for i in range(nA):
    total=0
    print("Ingrese la cantidad de notas del alumno", i+1)  
    nN=int(input())
    for j in range(nN):
        print(f"Ingrese la nota {j+1} del alumno {i+1}")
        nota=int(input())
        total+=nota
        promedio=total/nN
    print(f"El promedio del alumno {i+1} es {promedio}")

    if promedio>=40:
        print("Ha aprobado")
    else:
        print("Ha desaprobado")    
