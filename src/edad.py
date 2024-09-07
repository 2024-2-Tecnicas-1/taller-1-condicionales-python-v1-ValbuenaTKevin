from time import localtime
def evaluar(dia, mes, anno):
    hoy = localtime()
    edad = hoy.tm_year - anno
    if (hoy.tm_mon, hoy.tm_mday) < (mes, dia):
        edad -= 1
    return f"Usted tiene {edad} años"
if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día: ", end="")
    dia = int(input())
    print("Mes: ", end="")
    mes = int(input())
    print("Año: ", end="")
    anno = int(input())
    
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
