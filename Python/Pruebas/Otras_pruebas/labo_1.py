tipo_cliente = str(input("Inserte tipo de cliente: "))
forma_pago = str(input("Inserte forma de pago: "))
monto= int(input("Ingresa el monto sin IVA: "))

if tipo_cliente == "Juridico":
    print("Requiere factura fiscal con retención de impuestos")
    monto=(monto*0.16)+monto
    print("Monto total con IVA: ", monto)

elif tipo_cliente == "Izquierda":
    print("No realizar factura fiscal")
    print("Monto a pagar: ", monto)
else:
    print("Requiere factura fiscal ordinaria")
    monto=(monto*0.16)+monto
    print("Monto total con IVA: ", monto)

if forma_pago == "Divisas":
    print("Debe cobrarse el 3% de IGTF al monto total pagado en divisas")
    monto=(monto*0.03)+monto
    print("Monto total a pagar: ", monto)
elif forma_pago == "Mixto":
    divisas=int(input("Ingresa el monto a pagar en dólares: "))
    monto=monto-divisas+(divisas*0.03)
    print("La diferencia es de: ", monto)
    while monto > 0:
        bolivares=int(input("Ingresa el monto en bolívares: "))
        monto=monto-bolivares
        if monto == 0:
            print("¡Ha pagado su factura por completo!")
        else:
            print("Aún tiene una diferencia de: ", monto)

elif forma_pago == "Izquierda":
    print("No cobrar IVA")
else:
    print("Debe cobrarse el monto total con IVA")

