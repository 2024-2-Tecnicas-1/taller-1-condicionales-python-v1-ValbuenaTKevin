def evaluar(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido"
    if a == b == c:
        return "El triángulo es equilátero"
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles"
    else:
        return "El triángulo es escaleno"
if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
