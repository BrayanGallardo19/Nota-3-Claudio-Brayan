import libreria

opcion = 0
op5 = 0
#Menu de inicial para inicio de sesión
while opcion != 3:
    print("""\nBienvenido a FastMed (Medi)

1- Iniciar sesión
2- Registrarse
3- Salir""")

    try:
        opcion = int(input("\nIngrese su opción: "))
    except:
        print("\nLa opción ingresada no es valida, intente nuevamente ")

    match opcion:
        case 1:
#verifica si hubo 3 inicios fallidos y en caso de haberlo cierra el programa
            if libreria.iniciarsesion() == False: 
                break
            #Si las credenciales son correctas prosigue con el programa   
#esta primera muestra llega hasta aquí   
            else:
                while op5 != 4:
                    print("""Menu

1- Registrar hora de atención
2- Calculadora de costos de atención
3- Solicitar Movil de acercamiento
4- Salir""") 
                
                    try:
                        op5 = int(input("\n ingrese una opción: "))
                        if op5 ==1:
                            libreria.registrarhora()
                        if op5 == 2:
                            libreria.Calculo()
                        if op5 ==3:
                            libreria.movildeacercamiento(libreria.moviles)

                    except:
                        print("\nla opción ingresada no es valida")
#Funcion para registrar tus datos y crear tus credenciales de usuario
        case 2:
            libreria.registrarse()
        case 3:
            print("\nGracias por usar FastMed, ¡TENGA USTED UN GRAN DÍA!")