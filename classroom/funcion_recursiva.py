def calcular_numero_cuadrado(base,exponente):
    base = float(base)
    resultado = base**exponente
    exponente += 1

    if  resultado < 1000:
        print(resultado)
        calcular_numero_cuadrado(base,exponente)
    else:
        print("Sucesión terminada")

def main():
    calcular_numero_cuadrado(2,0)


if __name__ == '__main__':
    main()