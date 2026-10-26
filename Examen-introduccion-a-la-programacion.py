#Variable Global

Saldototal = 1000

#Funciones

def Deposito(plata):
    if plata < 0:
        print("La cantidad a de ser mayor que 0")
        return Saldototal
    else:
        resultado = plata + Saldototal
        return resultado


def retiro(plata):
    if  plata > Saldototal:
        print("No puede retirar mas dinero del que tiene disponible en su cuenta")
        return Saldototal
    else:
        resultado = Saldototal - plata
        return resultado


def leerOpcion():
    opcion = input(">>>Opcion? ")
    while opcion < "0" or opcion > "3":
        print("<><> Error. Opción no válida. <><>")
        input("Presione enter para continuar ....")
        menu()
        opcion = input("<> Opcion? <>")

    return int(opcion)


def ConsultarSaldo():
    print("\n\n\n 1. Consultar el saldo")

    print("\n Su saldo es de: ", Saldototal)


def Depositar():
    print("\n\n\n 2. Depositar dinero")

    Ingreso = int(input("\nIngrese la cantidad a depositar "))
    print("\nNuevo saldo: ", Deposito(Ingreso))
    return Deposito(Ingreso)


def Retirar():
    print("\n\n\n 3. Retirar Dinero")

    Sacarplata = int(input("\nIngrese la cantidad a retirar "))
    print("\nNuevo saldo: ", retiro(Sacarplata))
    return retiro(Sacarplata)


#Menu principal


def menu():
    print(
"""
*** MENU ***

1. Consultar saldo.
2. Depositar dinero.
3. Retirar dinero.
0. Salir.

************
""")

    

#Diferentes Opciones


while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            ConsultarSaldo()
        case 2:
            Saldototal = Depositar()
        case 3:
            Saldototal = Retirar()
        case 0:
            print("Gracias por usar nuestro cajero automatico. Hasta pronto!")
            break

    input("Presione Enter para continuar...")