Usuario = input("Por favor ingrese su nombre de usuario: ")

# Se cuenta la cant de intentos para acceder

counter = 0
while counter < 3:
    password = int(input('Por favor ingrese su contraseña de cuatro digitos: '))
    if password == 1234:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña equivocada.")
        counter += 1
if counter == 3:
    print("Acceso bloqueado. Cantidad de intentos excedidos.")
else:
    dinero = 2000
    print("Tu saldo actual es de $", dinero)
    print("¿Qué desea hacer a continuación?")

    movimientos_ingresos = []
    movimientos_retiros = []

    def opciones_de_usuario():
    
        print("Marque 0 para", "Depositar", "\nMarque 1 para", "Retirar", "\nMarque 2 para", "Estado de cuenta", "\nMarque 3 para", "Transferir", "\nMarque 4 para salir")
    
        opcion = None

        while opcion != 4:

            opcion = int(input("Ingrese un numero entre 0 y 4: "))

            if opcion == 0:
                print("Ha elegido la opcion de depositar.")
                deposito = int(input("Ingrese el monto que desea depositar: "))
                movimientos_ingresos.append(deposito)
                global dinero #Global a la variable dinero
                dinero += deposito
                print("Su saldo es: ", "$", dinero)

            if opcion == 1:
                print("Ha elegido la opción de retirar.")
                retiro = int(input("Ingrese el monto que desea retirar de su cuenta: "))
                movimientos_retiros.append(retiro)
                dinero -= retiro
                print("Su saldo disponible es: $", dinero)

            if opcion == 2:
                print("Ha elegido la opción de visualizar su estado de cuenta.")
                print("Su saldo actual es de: $", dinero)
                print("Sus movimientos de ingreso son: ", movimientos_ingresos[:], "\nSus movimientos de retiro son: ", movimientos_retiros[:])

            if opcion == 3:
                print("Ha elegido la opción de transferir.")
                verif = 0
                otra_cuenta = int(input("Las cuentas cuenta con nueve digitos. \nPor favor ingrese el número de cuenta al que desea transferir: "))
                print("Usted ha ingresado el siguiente numero de cuenta: ", otra_cuenta)
                verif = int(input("Marque 0 si es correcto. \nMarque 1 si no es correcto: "))
                if verif == 0:
                    print("La cuenta a la que desea transferir ha sido verificada.")
                    transf = int(input("Ingrese el monto que desea transferir: "))
                    movimientos_retiros.append(transf)
                    dinero -= transf
                    print("Usted ha transferido con éxito $", transf, "\nSu saldo actual es de: $", dinero)
                elif verif == 1:
                    print("Cuenta errada. Transferencia rechazada.")
                
            if opcion == 4:
                print("Sesión finalizada. \nGracias por preferirnos.")
        
    opciones_de_usuario()