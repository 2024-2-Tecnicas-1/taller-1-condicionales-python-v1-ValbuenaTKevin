def evaluar(num_victorias_a, num_victorias_b):
    if num_victorias_a < 0 or num_victorias_b < 0:
        return "Inválido"
    if num_victorias_a > 7 or num_victorias_b > 7:
        return "Inválido"
    if num_victorias_a >= 6 and num_victorias_a >= num_victorias_b + 2:
        return "Ganó A"
    if num_victorias_b >= 6 and num_victorias_b >= num_victorias_a + 2:
        return "Ganó B"
    
    if num_victorias_a == 5 and num_victorias_b == 7:
        return "Ganó B"
    if num_victorias_b == 5 and num_victorias_a == 7:
        return "Ganó A"  
    if num_victorias_a == 6 and num_victorias_b == 7:
        return "Ganó B"
    if num_victorias_b == 6 and num_victorias_a == 7:
        return "Ganó A"
    if (num_victorias_a >= 0 and num_victorias_a < 6) or (num_victorias_b >= 0 and num_victorias_b < 6):
        return "Aún no termina"
    
    return "Inválido"

if __name__ == '__main__':
    print("Juegos ganados por A:", end=" ")
    num_victorias_a = int(input())
    print("Juegos ganados por B:", end=" ")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
