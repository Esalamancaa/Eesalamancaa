# #Practica de if/while, integración de break

# intentos=3

# while intentos>0:
#     intentos-=1        
#     color=input("Ingrese un color :")

#     if color.lower()!="negro":
#         print("El color no es el requerido")
#     else:
#         print("Este es el color requerido")
#         break

#------------------------------------------------------#

# #Menú con varias preguntas

# #La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# #Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o más=>4%
# #Preguntar al usuario en qué comuna vive.
# #Preguntar al usuario con cuantas personas vive.
# #El arancel actual es de $200.000 por semestre.
# #Basados en las respuestas del usuariom y en la informacion dada, calcular su descuento.

# print('''
#       "Ingrese la comuna donde vive"
#     1.- La Florida 2.-La Pintana 3.- Puente Alto 4.-San Joaquin    
#     ''')
# comuna=int(input())

# print("¿Cuantas personas viven con usted")
# personas=int(input())

# if comuna==1:
#     desc=20
# elif comuna==2:
#     desc=30
# elif comuna==3:
#     desc=25
# elif comuna==4:
#     desc=15
# else:
#     print("No es una opción válida, intentelo de nuevo")

# if personas==1:
#     desc+=2
# elif personas>=2 and personas <=4:
#     desc+=3
# else:
#     desc+=4     

# arancel=int(200000-(200000*(desc/100)))
# print(f"El arancel final según los datos ingresados es: {arancel}")
# print(f"El descuento es de : {200000*(desc/100)}")

#------------------------------------------------------#

#Poner listado de 3 productos por categoria, las cat son 1,2 y 3
#Clasificar segun categoria y precio
#Cat 1 +200, cat 2 +400, cat 3 +600
#Precios: 1000 y menos, 3%; entre 1001 y 5000, 5% ; 5001 y más, 6%
#Agregar los impuestos segun la categoria  
#Luego aplicar descuento al total de la boleta según el monto

desc=0
pc1=0

print('''
      Bienvenido(a), elija una categoría :"
      1.- Conservas
      2.- Granos envasados
      3.- Jugos
      ''')
op=int(input())


if op==1:
    print('''
        Conservas
        1.- Jurel en lata $1800
        2.- Duraznos en almíbar $1500
        3.- Champiñones laminados $2000   
        0.- Salir     
          ''')
    op2=int(input())
    while op2!=0:
        if op2==1:
            print("Ha elegido jurel en Lata")
            desc+=5
            pc1+=1800+200
        elif op2==2:
            print("Ha elegido duraznos en almíbar")
            desc+=5
            pc1+=1500+200
        elif op2==3:
            print("Ha elegido duraznos en almíbar")
            desc+=5
            pc1+=2000+200 
        else:
            op2=int(print("Elija una opción válida"))
        op2=int(input())
 

