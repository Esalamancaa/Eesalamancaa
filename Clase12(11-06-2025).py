 #Tarea

 #Crear programa de manejo de notas
 #1.- Ingresar nota
 #2.- Borrar nota
 #3.- Mostrar notas
 #4.- Sacar promedio, nota mayor y nota menor
 #5.- Limpiar todas las notas
 #6.- Salir

notas=[6.2,6.4,5.2,5.5,6.0]
while True:
    while True:
        try:
            print('''
            Sistema de administración de calificaciones
            1.- Ingresar nota
            2.- Borrar nota
            3.- Mostrar notas
            4.- Sacar promedio. Nota mayor y menor
            5.- Borrar las notas  
            6.- Salir                                   
                ''')
            op=int(input())
            break
        except Exception:
            print("Ingrese un número entero")    
    match op:
        case 1:
            print("Ingrese la nota que quiere añadir")
            nota=float(input())
            notas.append(nota)
        case 2:
            print(notas)
            nota=float(input("Ingrese la nota que quiere remover: "))
            notas.remove(nota)
        case 3:
            print("Las notas ingresadas son:")
            for i in range(len(notas)):
                    print(f"{i+1}.- {notas[i]} ") 
        case 4:
            if len(notas)==0:
                print("No hay datos para esta acción")
            else:
                promedio=sum(notas)/len(notas)
                print(f"EL promedio de las notas es: {round(promedio,1)}")        
                print(f"La nota mayor es: {max(notas)}")   
                print(f"La nota menor es: {min(notas)}")     
        case 5:
            notas.clear()
        case 6:
            print("En construcción...")
        case 7:
            print("Saliendo del sistema...")  
            break          
        case _:
            print("No es una opción válida, vuelva a intentar")

#-------------------------------------------------------------------------------------------------------------------#  

# #VerProfe

# notas=[6.2,6.4,5.2,5.5,6.0]
# while True:
#     while True:
#         try:
#             print('''
#             Sistema de administración de calificaciones
#             1.- Ingresar nota
#             2.- Borrar nota
#             3.- Ver notas
#             4.- Promedio de notas. Nota mayor y menor
#             5.- Borrar las notas      
#             6.- Salir                               
#                 ''')
#             op=int(input())
#             break
#         except Exception:
#             print("Ingrese un número entero")    
#     match op:
#         case 1:
#             print("Ingrese la nota que quiere añadir")
#             nota=float(input())
#             notas.append(nota)
#         case 2:
#             for num, n in enumerate(notas):
#                 print(num+1,".-",n)
#             nota=int(input("Ingrese la nota que quiere remover: "))
#             notas.pop(nota-1)
#         case 3:
#             for n in notas:
#                 print(n)
#         case 4:
#             if len(notas)==0:
#                 print("No hay notas para sacar el promedio")
#             else:
#                 promedio=sum(notas)/len(notas)
#                 print(f"EL promedio de las notas es: {round(promedio,1)}")        
#             print(f"La nota mayor es: {max(notas)}")   
#             print(f"La nota menor es: {min(notas)}") 
#         case 5:
#             notas.clear()
#         case 6:
#             print("Saliendo...")
#             break
#         case _:
#             print("No es una opción válida, vuelva a intentar")     

#-------------------------------------------------------------------------------------------------------------------#  

# notas=[4.6, 7.0, 5.6]

# for num, n in enumerate(notas):
#     print(num+1,".-",n)

# n=int(input("Seleccione una nota: "))
# print("El usuario seleccionó la nota", notas[n-1])

#-------------------------------------------------------------------------------------------------------------------#  

#append() Pone un elemento al final de la lista
#sum() suma todos los elementos de la lista
#max() muestra el elemento mayor
#min() muestra el elemento menor
#len() muestra el largo del objeto
#pop() elimina un elemento por el indice
#remove() elimina un elemento por el valor
#clear() limpia la lista completa
#insert() inserta un elemento en el indice indicado
#enumerate() enumera la lista con otro argumento
#extend() agrega varios elementos a la lista
#sort() ordena la lista de mayor a menor
#reverse() voltea la lista

#-------------------------------------------------------------------------------------------------------------------#  

lc=[[3,4],[8,9]]

print(lc[0][1])