def evaluar(a, b, c):
    tipo_de_triangulo=""
    if ((a + b > c) & (a + c > b) & (b + c > a)):
        if(a == b & b == c):
            tipo_de_triangulo = "El triángulo es equilátero"
        elif(a == b | a == c | b == c):
            tipo_de_triangulo = "El triángulo es isósceles"
        else:
            tipo_de_triangulo = "El triángulo es escaleno"
    else:
        tipo_de_triangulo = "No es un triángulo válido"        

    return tipo_de_triangulo

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
