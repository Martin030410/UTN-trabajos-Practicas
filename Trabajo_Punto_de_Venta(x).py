#Punto de Venta (Fast Food) Creen un programa para gestionar los pedidos de un local de comida rápida. El programa debe tener un menú que le permita al cajero ir sumando productos a la cuenta de un cliente. Menú principal: 1. Agregar Hamburguesa ($4500) 2. Agregar Papas Fritas ($2000) 3. Agregar Bebida ($1500) 4. Pagar el pedido (Cierra el ticket) 5. Cancelar pedido y salir Requisitos: • Cada vez que se elige la opción 1, 2 o 3, se debe sumar el precio al total y avisar por pantalla ("Hamburguesa agregada. Total actual: $..."). • Si se elige Pagar (Opción 4), el programa debe mostrar el total a pagar y pedirle al cajero que ingrese con cuánto efectivo paga el cliente. • ¡Atención! Si el efectivo ingresado es menor al total, el programa debe usar un bucle while para seguir pidiendo dinero hasta que alcance o supere el total. Una vez que alcanza, debe mostrar el cambio (vuelto) a devolver al cliente, reiniciar el total a $0 y volver al menú principal para el siguiente cliente. • La opción 5 finaliza el programa por completo. 


total = 0
while True:
    print("Bienvenido al Punto de Venta de Comida Rápida")
    print("Menú de opciones:")
    print("1. Agregar hamburguesa ($4500)")
    print("2. Agregar papas fritas ($2000)")
    print("3. Agregar bebida ($1500)")
    print("4. Pagar el pedido (cierra el ticket)")
    print("5. Cancelar pedido y salir")
    opcion= input("Ingrese una opcion: ")
    match opcion:
        case "1":
            total += 4500
            print(f"Hamburguesa agregada. Total actual: ${total}")
        case "2":
            total += 2000
            print(f"Papas fritas agregadas. Total actual: ${total}")
        case "3":
            total += 1500
            print(f"Bebida agregada. Total actual: ${total}")
        case "4":
            if total == 0:
                print("El pedido está vacío. Agregue productos primero.")
                continue
            print(f"Total a pagar: ${total}")
            
            efectivo = input("Ingrese el efectivo con el que paga el cliente: ")
            while not efectivo.isdigit() or float(efectivo) < total:
                print("Efectivo insuficiente. Por favor, ingrese un monto válido.")
                efectivo = input("Ingrese el efectivo con el que paga el cliente: ")
                
            efectivo = float(efectivo)
            cambio = efectivo - total
                
            print(f"Pago recibido: ${efectivo}. Cambio a devolver: ${cambio}")
            print ("Gracias por su compra. ¡Hasta luego!")
            break
        case "5":
            print("Pedido cancelado. Saliendo del programa.")
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")