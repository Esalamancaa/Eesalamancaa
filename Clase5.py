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

#Menú con varias preguntas

#La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
#Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o más=>4%
#Preguntar al usuario en qué comuna vive.
#Preguntar al usuario con cuantas personas vive.
#El arancel actual es de $200.000 por semestre.
#Basados en las respuestas del usuariom y en la informacion dada, calcular su descuento.

print('''
      "Ingrese la comuna donde vive"
    1.- La Florida 2.-La Pintana 3.- Puente Alto 4.-San Joaquin    
    ''')
comuna=int(input())

print('''
      ¿Cuantas personas viven con usted?
      ''')
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