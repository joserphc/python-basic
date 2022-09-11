def main():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue # No se va a ejecutar
    #     print(contador)

    # for i in range(1000):
    #     print(i)
    #     if i == 567:
    #         break

    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    main()