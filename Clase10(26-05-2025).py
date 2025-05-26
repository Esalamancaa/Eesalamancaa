# #Actividad formativa menús

# import time
# import os

# deuda=100000

# print("Bienvenido al servicio de tu tarjeta de crédito")
# time.sleep(2)
# print("Presione enter para continuar")
# enter=input()
# os.system('cls')


# while True:
#     print('''
#     Elija la operación que quiere realizar:
#     1.- Ver deuda         2.- Pagar cuenta   
#     3.- Realizar compra   0.- Salir               
#         ''')
#     try:
#         op=int(input())
#         os.system('cls')
#         match op:
#             case 1:
#                 print(f"Su deuda es ${deuda}")
#                 time.sleep(1)
#                 os.system('cls')
#             case 2:
#                 try:
#                     print("Ingrese el pago que va a realizar a su cuenta")
#                     pago=int(input())
                
#                     if pago<=deuda:
#                         deuda-=pago
#                         print(f"Su deuda actual es de ${deuda}")   
#                         time.sleep(1)
#                         os.system('cls') 
#                     elif pago<=0:
#                         print("No puede utilizar 0 o número negativos en este apartado")        
#                     else:
#                         while pago>deuda:
#                             print(f"Ha ingresado un monto mayor a la deuda, que es ${deuda}, ingrese un valor válido.")
#                             pago=int(input())
#                 except Exception:
#                     print("Ingrese un valor en numeros enteros")            
#             case 3:
#                 try:
#                     print("¿Cuál es el monto de la compra que va a realizar?")
#                     compra=int(input())
#                     if compra>0:
#                         deuda+=compra
#                         print(f"Ha gastado ${compra} de su cuenta, su deuda ahora es de {deuda}")    
#                         time.sleep(1)
#                         os.system('cls')
#                     else:
#                         print("La compra no puede ser menor o igual a 0")    
#                 except Exception:
#                     print("Ingrese un valor en numeros enteros")        
#             case 0:
#                 os.system('cls')
#                 print("Saliendo del sistema...")
#                 time.sleep(2)
#                 break    
#             case _:
#                 print("Ingrese una opción válida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros, prefiera: 1, 2, 3 ,4 o 0") 

#-------------------------------------------------------------------------------------------------------------------------------------------------#

# #Menú registro de usuarios

# import time
# import os

# user1=None ; pass1=None
# user2=None ; pass2=None
# user3=None ; pass3=None

# print("Bienvenido al sistema de usuarios")
# time.sleep(1)
# print("Ingrese cualquier tecla para continuar")
# enter=input()
# os.system('cls')

# while True:
#     while True:
#         try:
#             print('''
#     Elija lo que quiere hacer:              
#     1.- Iniciar sesión
#     2.- Registrar usuario
#     3.- Salir                            
#                 ''')
#             op=int(input())
#             os.system('cls')
#             break
            
#         except Exception:
#             print("Debe ingresar un número entero")

#     match op:
#         case 1: 
#             print("Ingrese su usuario:")
#             user=input()
#             if user==user1:
#                     print("Ingrese su contraseña")
#                     cc=input()
#                     while True:
#                         if cc==pass1:
#                             print('''
#                         ¿Qué es lo que quiere hacer?
#                         1.- Realizar llamada
#                         2.- Enviar correo electronico
#                         3.- Cerrar sesión                                              
#                                 ''')
#                             op2=int(input())
#                             match op2:
#                                 case 1:
#                                     print("Marcar número")
#                                     num=int(input("9 "))
#                                 case 2:
#                                     print("Ingrese su correo")
#                                     correo=input()    
#                                 case 3:
#                                     print("Cerrando sesión...")
#                                     break    
#                         else:
#                             while cc!=pass1:
#                                 print("Contraseña incorrecta, reintente")
#                                 cc=input()        
#             elif user==user2:
#                     print("Ingrese su contraseña")
#                     cc=input()
#                     while True:
#                         if cc==pass2:
#                             print('''
#                         ¿Qué es lo que quiere hacer?
#                         1.- Realizar llamada
#                         2.- Enviar correo electronico
#                         3.- Cerrar sesión                                              
#                                 ''')
#                             op2=int(input())
#                             match op2:
#                                 case 1:
#                                     print("Marcar número")
#                                     num=int(input("9 "))
#                                 case 2:
#                                     print("Ingrese su correo")
#                                     correo=input()    
#                                 case 3:
#                                     print("Cerrando sesión...")
#                                     break    
#                         else:
#                             while cc!=pass2:
#                                 print("Contraseña incorrecta, reintente")
#                                 cc=input()    
#             elif user==user3:
#                     print("Ingrese su contraseña")
#                     cc=input()
#                     while True:
#                         if cc==pass3:
#                             print('''
#                         ¿Qué es lo que quiere hacer?
#                         1.- Realizar llamada
#                         2.- Enviar correo electronico
#                         3.- Cerrar sesión                                              
#                                 ''')
#                             op2=int(input())
#                             match op2:
#                                 case 1:
#                                     print("Marcar número")
#                                     num=int(input("9 "))
#                                 case 2:
#                                     print("Ingrese su correo")
#                                     correo=input()    
#                                 case 3:
#                                     print("Cerrando sesión...")
#                                     break    
#                         else:
#                             while cc!=pass3:
#                                 print("Contraseña incorrecta, reintente")
#                                 cc=input()
#             else:
#                 print("Ingrese un usuario valido")                

#         case 2:
#             while True:
#                 try:
#                     print('''¿Qué usuario quiere ingresar o modificar?
#                           1.- Usuario 1
#                           2.- Usuario 2
#                           3.- Usuario 3
#                           ''')
#                     op3=int(input())
#                     match op3:
#                         case 1:
#                             print("Ingrese el nombre de usuario")
#                             user1=input()
#                             print(f"Su usuario ha sido actualizado a {user1}")
#                             time.sleep(1)
#                             print("Ingrese una contraseña para su usuario")
#                             pass1=input()
#                             break
#                         case 2:
#                             print("Ingrese el nombre de usuario")
#                             user2=input()
#                             print(f"Su usuario ha sido actualizado a {user1}")
#                             time.sleep(1)
#                             print("Ingrese una contraseña para su usuario")
#                             pass2=input()
#                             break
#                         case 3:
#                             print("Ingrese el nombre de usuario")
#                             user3=input()
#                             print(f"Su usuario ha sido actualizado a {user1}")
#                             time.sleep(1)
#                             print("Ingrese una contraseña para su usuario")
#                             pass3=input()   
#                             break   
#                         case _:
#                             print("Ingrese una opción válida")      

#                 except Exception:
#                     print("Ingrese solamente letras")    
#         case 3:
#             print("Saliendo...")    
#             break       

#-------------------------------------------------------------------------------------------------------------------------------------------------#

user1=None ; pass1=None
user2=None ; pass2=None
user3=None ; pass3=None

while True:
    op=int(input('''
            Seleccione una opción:
            1.- Iniciar sesión
            2.- Registrar usuario
            3.- Salir               
                 '''))
    match op:
        case 1:
            if user1==None and user2==None and user3==None:
                print("No hay usuarios registrados")
            else:
                print("Ingrese su usuario")
                user=input()
                password=input("Ingrese su contraseña :")   
                if (user == user1 and password == pass1) or (user == user2 and password == pass2) or (user == user3 and password == pass3):
                    print('''
                    1.- Realizar llamada
                    2.- Enviar correo electronico
                    3.- Cerrar sesión            
                            ''')
        case 2:
            pre=int(input("¿Qué usuario registrará?, 1, 2, 3"))
            match pre:
                case 1:
                    user1=user
                    pass1=password
                case 2:
                    user2=user
                    pass2=password
                case 3:
                    user3=user
                    pass3=password
                case _:
                    print("Opción inválida")
        case 3:
            break
        case _:
            print("Opción válida")