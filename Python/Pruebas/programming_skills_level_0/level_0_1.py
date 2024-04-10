username = input("Ingresa tu nombre de usuario: ")
password = input("Inserta tu contraseña: ")
base = "skills.01"

while password != base:
    if password == base:
        print("Usted ha ingresado efectivamente a su cuenta de banco, su saldo es $2000")
    elif password != base:
        for i in range(2):
            print()
    else:
        break
        print("Su cuenta ha sido bloqueada temporalmente")
        