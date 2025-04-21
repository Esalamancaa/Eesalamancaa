# prom=suma/cant
# print("El promedio es", prom)

#------------------------------------------------------#

#Pida la cantidad de alumnos y luego la cantidad de notas por alumno
#Muestre el promedio de cada uno

# cantA=int(input("Ingrese el numero de alumnos"))

# for j in range(cantA):
#     print("Ingrese el numero de notas")
#     cantN=int(input())
#     for i in range(cantN):
#         print("Ingrese nota", i+1, "del alumno", j+1, "(use valores decimales)")
#         nota=float(input())
#         suma=0
#         suma+=nota
#     prom=suma/cantN
#     print("El promedio es ", prom)
#     if prom>=4:
#         print("Usted aprobó")
#     else:
#         print("Usted reprobó")     

#------------------------------------------------------#

#Pida al usuario un numero y sume todos los digitos desde el 1 hasta el numero mostrando la suma.

num=int(input("Ingrese un numero"))
suma=0

for i in range(num):
    suma+=1
print("La suma de los numeros es", suma)