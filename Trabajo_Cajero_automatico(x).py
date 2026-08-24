#Desarrollen un simulador de cajero automático. El usuario comenzará con un saldo inicial de $50,000. El programa debe mostrar un menú que se repita hasta que el usuario decida salir: 
# 1) Consultar saldo
# 2) ingresar dinero 
# 3) retirar dinero 
# 4)salir
#Reglas de negocio: • No se pueden ingresar cantidades negativas. • No se puede retirar más dinero del que hay en el saldo, ni cantidades negativas. Si el usuario intenta retirar de más, mostrar un mensaje de "Fondos insuficientes". • Usar match-case para manejar las opciones del menú.


print ("Cajero automatico")
saldo_inicial = 50000

while True:
    print("\nMenu de opciones:")
    opcion = input("""Ingrese una opcion
                1)consultar saldo
                2)ingrese dinero
                3)retirar dinero
                4)salir\n
    opcion: """)
    match opcion :
        case "1": 
            print(f"Su saldo actual es: ${saldo_inicial}")
        case "2":
            ingreso_str = input("Ingrese la cantidad a depositar: ")
            if not ingreso_str.isdigit():
                print("Error: Ingrese un número entero válido.")
            else:
                ingreso = float(ingreso_str)
                if ingreso <= 0:
                    print("El depósito debe ser mayor a 0.")
                else:
                    saldo_inicial += ingreso
                    print(
                        f"Se han ingresado ${ingreso}. Su nuevo saldo es: ${saldo_inicial}"
                    )
        case "3":
            retiro_str = input("Ingrese la cantidad a retirar: ")
            if not retiro_str.isdigit():
                print("Error: Ingrese un número entero válido.")
                continue
            retiro = float(retiro_str)
            if retiro < 0:
                print("No se pueden retirar cantidades negativas.")
            elif retiro > saldo_inicial:
                print("Fondos insuficientes.")
            else:
                saldo_inicial -= retiro
                print(f"Se han retirado ${retiro}. Su nuevo saldo es: ${saldo_inicial}")
        case "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")