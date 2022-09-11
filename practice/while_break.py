def main():
    NUM_LIMITE = 1000
    contador = 0

    while contador < NUM_LIMITE:
        print(contador*2)
        contador += 1
        if contador == 20:
            break
        

if __name__ == '__main__':
    main()