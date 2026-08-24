#El Horno Industrial Estás programando el panel de control de un horno industrial. El operador debe ingresar por teclado la temperatura actual para registrarla, pero a veces teclean mal (ingresan letras, varios puntos, o dejan vacío). Si el programa intenta convertir un texto erróneo a decimal, el sistema se cae. Tu misión: Crea un programa que pida continuamente la temperatura y la valide. Reglas: 1. El programa debe pedir temperaturas hasta que el usuario escriba exactamente la palabra "FIN". 2. Para saber si el texto ingresado se puede convertir a float, debes revisarlo. Un texto es un número decimal válido (positivo) si: o No está vacío ni es solo un punto ("."). o Contiene únicamente números y, como máximo, un solo punto. 3. Si el texto tiene letras, símbolos raros o más de un punto (ej: 12.3.4), debes mostrar un error y volver a pedir el dato. 4. Solo cuando estés 100% seguro de que el texto es válido, conviértelo usando float(temperatura_str). 5. Una vez convertido, si la temperatura es menor a 100.0 o mayor a 500.0, el sistema debe imprimir: "¡ADVERTENCIA! Temperatura fuera de rango", pero registrarla igual. 

print("Panel de control del horno industrial")
while True:
    temperatura_str = input("Ingrese la temperatura actual (o escriba 'FIN' para salir): ")
    
    if temperatura_str == "FIN".lower():
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    if not temperatura_str or temperatura_str.count('.') > 1 or not all(c.isdigit() or c == '.' for c in temperatura_str):
        print("Error: Ingrese un número decimal válido.")
        continue
    
    temperatura = float(temperatura_str)
    
    if temperatura < 100.0 or temperatura > 500.0:
        print("¡ADVERTENCIA! Temperatura fuera de rango")
    
    print(f"Temperatura registrada: {temperatura}°C")
    