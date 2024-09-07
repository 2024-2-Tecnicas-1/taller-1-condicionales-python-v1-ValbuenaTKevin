def evaluar(caracter):
    if caracter.isdigit():
        return "Es número"

    elif caracter.isalpha():
        if caracter.isupper():
            return "Es letra mayúscula"
        elif caracter.islower():
            return "Es letra minúscula"
    
    return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input().strip()
        
    respuesta = evaluar(caracter)
    print(respuesta)
