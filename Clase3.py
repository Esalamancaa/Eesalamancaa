# #AutosYSuPeso
# auto=int(input("Auto liviano(1), auto pesado(2)"))

# al=0

# for i in range(auto):
#     if auto==1:
#         print("Auto liviano, el costo es de $5000")
#         al=al+5000
#     else:
#         print("Auto pesado, el costo es de $7000")   

#------------------------------------------------------#

# #CandidatosConteo

# #Definir 2 candidatos. Preguntar la cantidad de votantes.
# #Preguntar a ca davotante por quien votará mostrando las alternativas.
# #Contar los votos y mostrar resultados.
# #Definir el ganador y considerar un empate.

# c1="Aqua"
# c2="KOKU"
# cv1=0
# cv2=0
# cantV=int(input("¿Cuantos votantes son? :"))

# for i in range(cantV):
#     print(f"¿por quién votará? 1.- {c1}, 2.-{c2}")
#     voto=int(input())

#     if voto==1:
#         print(f"Ha votado por {c1}")
#         cv1+=1
#     elif voto==2:
#         print(f"Ha votado por {c2}")    
#         cv2+=1
#     else:
#         print("Elija una opción válida : 1 o 2")    

# if cv1>cv2:
#     print(f"Votaron {cantV} personas. El ganador es {c1}, con {cv1} votos")
# elif cv2>cv1:
#     print(f"Votaron {cantV} personas. El ganador es {c2}, con {cv2} votos")    
# else:
#     print("Es un empate")    

#------------------------------------------------------#    

# #Ver cuantas vocales tiene una palabra

# frase=input("Ingrese una frase ")
# c=0
# cons=0
# v=0

# for i in frase:

#     if i.lower() in "aeiou":
#         v+=1
#     else:
#         cons+=1
#     c+=1

# print(f"La cantidad de caracteres es {c} ")
# print(f"La cantidad de consonantes es {cons} ")
# print(f"La cantidad de vocales es {v} ")   
        
#------------------------------------------------------#    

# cant=int(input("Ingrese la cantidad de numeros: "))

# for i in range(cant):
#     num=int(input("Ingrese un numero"))
#     if num %2==0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")    

#------------------------------------------------------#    

# #Ingresar un numero, que muestre la sucesion de numeros y si son par o impar.

# num=int(input("Ingrese un numero"))
   
# for i in range(1, num+1):
#     if (i) %2==0:
#         print(i, "es numero par")
#     else:
#         print(i, "es numero impar")    

#------------------------------------------------------#    

# #Supermercado

# cant=int(input("Ingrese la cantidad de productos :"))
# total=0

# for i in range(cant):
#     print('''
#         ¿Qué producto llevará?
#         1.- Diazepam $9000
#         2.- Metametozona $18500
#         3.- Oblea China $1000          
#           ''')
#     op=int(input())

#     if op==1:
#         print("Usted lleva Diazepam")
#         total+=9000
#     elif op==2:
#         print("Usted lleva Metanetozona")
#         total+=18500
#     elif op==3:
#         print("Usted lleva Oblea China")
#         total+=1000
#     else:
#         print("Elija una opción válida: 1,2,3")

# print(f"El precio total de su compra es: {total} ")
# print(f"El precio final + IVA es: {total*1.19} ")