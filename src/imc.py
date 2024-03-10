def evaluar(peso, estatura, edad):
    imc = peso/(estatura*estatura)
    respuesta = ""
    if edad < 45:
        if imc<22.0:
            respuesta = "bajo"
        
        if imc>=22.0:
                respuesta = "medio"
            
    elif edad>=45:
            if (imc<22.0):
                respuesta = "medio"
            
            if (imc>=22.0):
                respuesta = "alto"
            
    


    return respuesta;

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
