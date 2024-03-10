def evaluar(numero1, numero2, numero3, numero4):
    resultado=""
    numeros = [numero1, numero2, numero3, numero4]
    for i in range(len(numeros)):
        min = i
        for j in range(i + 1, len(numeros)):
            if numeros[j] < numeros[min]:
                min = j
        numeros[i], numeros[min] = numeros[min], numeros[i]
    for numero in numeros:
        resultado += str(numero)+" "

    return resultado;

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
