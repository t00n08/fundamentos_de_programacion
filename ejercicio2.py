from random import randint

limite_inferior = int(input("Ingrese límite inferior: "))
limite_superior = int(input("Ingrese límite superior: "))

numero_secreto = randint(limite_inferior, limite_superior)

if numero_secreto % 2 != 0:
    if (numero_secreto + 1) <= limite_superior:
        numero_secreto = numero_secreto + 1
    else:
        numero_secreto = numero_secreto - 1

intento1 = int(input("Intente adivinar: "))

if intento1 == numero_secreto:
    print("Felicitaciones, pudiste adivinar.")
else:
    if numero_secreto > intento1:
        print("El número es mayor.")
    else:
        print("El número es menor.")
        
    intento2 = int(input("Intente de nuevo: "))
    
    if intento2 == numero_secreto:
        print("Felicitaciones, pudiste adivinar.")
    else:
        if numero_secreto > intento2:
            print("El número es mayor.")
        else:
            print("El número es menor.")
            
        distancia1 = abs(numero_secreto - intento1)
        distancia2 = abs(numero_secreto - intento2)
        
        print("Te daré una pista:")
        if distancia2 < distancia1:
            print(f"El número que buscas está más cerca de {intento2} que de {intento1}")
        else:
            print(f"El número que buscas está más cerca de {intento1} que de {intento2}")
            
        intento3 = int(input("Intente la última vez: "))
        
        if intento3 == numero_secreto:
            print("Felicitaciones, pudiste adivinar.")
        else:
            print("Perdiste.")
            print(f"El número era: {numero_secreto}")