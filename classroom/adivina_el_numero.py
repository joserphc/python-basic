import random

def main():
    random_number = random.randint(1, 100)
    choose_number = int(input('Elige un número del 1 al 100: '))
    while choose_number != random_number:
        if choose_number < random_number:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
            
        choose_number = int(input('Elige otro número: '))
    print('¡Ganaste')

if __name__ == '__main__':
    main()