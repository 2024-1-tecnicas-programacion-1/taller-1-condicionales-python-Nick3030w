from datetime import datetime
def evaluar(dia, mes, anno):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime(anno, mes, dia)
    diferencia = fecha_actual - fecha_nacimiento
    edad = diferencia.days // 365
    respuesta="Usted tiene ", edad, " años"
    return respuesta;

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
