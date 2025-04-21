# nombre="Esteban"
# edad=22

# print("Hola", nombre, ", su edad es", edad)

# # Solicitud de datos
# print("Ingrese su nombre")
# nombre=input()

# print("Ingrese su edad")
# edad=input()    
# # Ejemplo de concatenacion

# print("Hola", nombre, ", su edad es", edad)

# print("Ingrese el primer numero")
# n1=int(input())
# print("Ingrese el segundo numero")
# n2=int(input())

# print("El resultado de la suma es ", n1+n2)

#Ingresar tres numeros y sacar el promedio

# print("Ingrese tres numeros para sacar su promedio")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# prom=(n1+n2+n3)/3
# print("El promedio es", prom)

# if prom>=40:
#     print("El alumno aprobó")
# else:    
#     print("El alumno reprobó")

#Pedir edad al usuario y determinar si es mayor de edad

# print("Ingrese su edad")
# edad=int(input())

# if edad>=18:
#     print("Usted tiene", edad, "años, es mayor de edad")
# else:
#     print("Usted tiene", edad, "años, es menor de edad")  

# Mostrar segun criterio. 
# Menos de 12 años es niño
# Entre 12 y 17 años es adolescente
# Entre 18 y 64 años es adulto
# 65 o más, es adulto mayor
     
# print("Ingrese su edad")
# edad=int(input())

# if edad<12:
#     print("Usted es un niño")
# elif edad>=12 and edad<18:
#     print("Usted es adolescente")
# elif edad>=18 and edad<65:    
#     print("Usted es adulto")
# else: 
#     print("Ustes es adulto mayor")       

#Ingresar 3 numeros y mostrar el mayor de los tres

print("Ingrese el primer numero")
n1=int(input())
print("Ingrese el segundo numero")
n2=int(input())
print("Ingrese el tercer numero")
n3=int(input())

if n1>n2 and n2>n3:
    print("El numero mayor es", n1)
elif n2>n1 and n2>n3:
    print("El numero mayor es", n2)
else:
    print("El numero mayor es", n3)  