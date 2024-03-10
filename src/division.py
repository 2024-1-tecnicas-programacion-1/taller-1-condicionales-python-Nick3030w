def evaluar(dividendo, divisor):
    cociente = 0
    residuo = 0
    exacta=""
    residuo=dividendo%divisor
    cociente=int(dividendo/divisor)
    if (residuo==0):
        exacta="es"
    else:
        exacta="no es"
    respuesta = "La división " + exacta + " exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
