id = [1]
usuarios = ["DUOCUC"]
contraseñas = ["DUOC123"]
nombres = ["DUOCUC"]
segundosnombres = [None]
apellidosp = [None]
apellidosm = [None]
ruts = [193214495]
discapacidades = [None]
numerostelefono = [920867215]
nuevousuario = None
horastomadas = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
moviles = 5
serv =[]
opcion = 0
#verifica tu inicio de sesion, si hay 3 intentos fallidos cierra el programa automaticamente
def iniciarsesion():
    contador = 0
    while True:
        user = input("\nIngrese su usuario: ")
        password = input("\nIngrease su contraseña: ")

        if user in usuarios and password in contraseñas:
                print(f"\nBienvenido {user}")
                return True
        else:
                print("\nEl usuario ingresado no es valido")
                contador +=1
        if contador == 3:
                print("\nDemasiados intentos, gracias por usar Fast Med")
                return False    
#registra tus datos y crea tus credenciales de acceso según las reglas del negocio
def registrarse():
    id.append(len(id)+1)
    while True:
        nombre = input("\nIngrese su nombre: ")
        if nombre != "":
              nombres.append(nombre)
              nuevousuario = nombre[0]
              break
        else:
              print("\nEl nombre ingresado no es valido, intente nuevamente")
    while True:
        segnombre = input("\nIngrese su segundo nombre: ")
        if segnombre != "":
              segundosnombres.append(segnombre)
              break
        else:
              print("\nEl nombre ingresado no es valido, intente nuevamente")              
    while True:
        apep = input("\nIngrese su apellido paterno: ")
        if apep != "":
              apellidosp.append(apep)
              nuevousuario = nuevousuario + apep[0]
              break
        else:
              print("\nEl apellido ingresado no es valido, intente nuevamente")
    while True:
        apem = input("\nIngrese su apellido materno: ")
        if apem != "":
              apellidosm.append(apem)
              break
        else:
              print("\nEl apellido ingresado no es valido, intente nuevamente")
    while True:
        numeros = ['1','2','3','4','5','6','7','8','9','k']
        rut = input("\nIngrese su Rut (sin puntos ni guión): ").lower()
        conteo = 0
        for r in rut:
              if r in numeros:
                   conteo += 1
        if conteo == 8 or conteo == 9:
            ruts.append(rut)
            nuevousuario = nuevousuario + rut [0] + rut[1] + rut[2]
            break
        else:
              print("\nEl Rut ingresado no es valido, intente nuevamente")
    while True:
          disc = input("\n¿Tiene usted alguna discapacidad? responda si o no: ").lower()          
          if disc == "si" or disc == "no":
                break
    while True:
            numero = input("\nIngrese su numero de telefono (9 numeros ejemplo: 920867215): ")
            numeros = ['1','2','3','4','5','6','7','8','9']
            conteo = 0
            for x in numero:
                 if x in numeros:
                      conteo += 1
            if conteo == 9:
                  numerostelefono.append(numero)
                  nuevousuario = nuevousuario + numero[-4] + numero[-3] + numero[-2] + numero[-1]
                  break
            else:
              print("\nEl numero ingresado no es valido")      
    contraseñas.append(nuevousuario.upper())
    usuarios.append(rut)

def registrarhora():
     while True:
            print("""\n
ingrese la hora a la que desea agendar: 
           
1- 01:00 AM 
2- 02:00 AM 
3- 03:00 AM 
5- 05:00 AM 
7- 07:00 AM 
9- 09:00 AM  
10- 10:00 AM 
11- 11:00 AM  
12- 12:00 AM        
13- 13:00 PM 
14- 14:00 PM  
15- 15:00 PM  
16- 16:00 PM        
17- 17:00 PM   
18- 18:00 PM 
19- 19:00 PM         
20- 20:00 PM        
21- 21:00 PM           
22- 22:00 PM         
23- 23:00 PM 
24- 00:00 PM """)
            while True:
                  try:
                        hora = int(input("\nIngrese su opción: "))
                        if hora in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
                              break
                        else:
                              print("\nLa opción ingresada no es valida")
                  except:
                        print("\nHora ingresada no es valida")
            if horastomadas[hora-1] > 0 and hora >= 0 and hora <=24:
                  horastomadas[hora-1] = horastomadas[hora-1]-1
                  print(f"\nSu hora fue ingresada con exito, lo esperamos a las {hora}:00")
                  print("")
                  break
            else:
                  print("\nLa hora ingresada no es valida")

def movildeacercamiento(moviles):
    print(f"Cantidad de moviles disponibles: {moviles} de 8AM a 22PM")
    
    while True:
        print("""Indique a cuál de nuestros centros médicos se dirige:
              
1- Monte Incahuasi 904, Quilicura
2- AV.Consistorial 204, Peñalolén
3- Las Cumbres 430, Macul""")
        
        try:
            op = int(input("\nIngrese su opción: "))
        except:
            print("Opción inválida. Por favor, ingrese un número válido.")
            continue
        
        if op == 1 or op == 2 or op == 3:
            while True:
                print("\nSeleccione la hora de llegada:")
                print("""
1- 8:00AM
2- 9:00AM
3- 10:00AM
4- 11:00AM
5- 12:00PM
6- 13:00PM
7- 14:00PM
8- 15:00PM
9- 16:00PM                             
10- 17:00PM
11- 18:00PM
12- 19:00PM
13- 20:00PM
14- 21:00PM                        
15- 22:00PM
""")
                try:
                    opc = int(input("Ingrese su opción: ")) 
                    if opc in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
                        break
                except :
                    print("Hora ingresada no válida. Intente nuevamente.")
                    continue
                
            if opc in range(1, 16):
                moviles -= 1
                print(f"\nSu visita movil ha sido agendada a las {opc + 7}:00.")
                print(f"Quedan {moviles} móviles disponibles.")
                print("\nSu ubicación será rastreada por la aplicación, por favor mantenga esta opción activada")
                break
            else:
                print("Opción de hora no válida. Por favor, elija una opción válida.")
        else:
            print("Opción de centro médico no válida. Por favor, elija una opción válida.")

def Calculo():
    print("""
Servicios Psicologicos
1- Psicología Clínico: $8000
2- Psiquiatría: $15000
3- Evaluación Psicológica Integral: $18000
4- Terapia Psicoanalítica: $15000
5- Terapia de Pareja: $13000
6- Terapia Familiar: $13000
7- Salir
""")


    while True:
        opcion= int(input("Ingrese el servicio que desee:"))
        if opcion == 1:
            print("\nPsicología Clínico: $8.000\n")
            serv.append(8000)

        elif opcion ==2:
            print("\nPsiquiatría: $15.000\n")
            serv.append(15000)

        elif opcion == 3:
            print("\nEvaluación Psicológica Integral: $18000\n")
            serv.append(18000)

        elif opcion == 4:
            print("\nTerapia Psicoanalítica: $15000\n")
            serv.append(15000)

        elif opcion == 5:
            print("\nTerapia de Pareja: $13000\n")
            serv.append(13000)

        elif opcion == 6:
            print("\nTerapia Familiar: $13000\n")
            serv.append(13000)

        elif opcion == 7:
            precio_final=sum(serv)
            print("\nEl precio final es de $", precio_final)
            break
        else:
             print("la opción ingresada no es valida")