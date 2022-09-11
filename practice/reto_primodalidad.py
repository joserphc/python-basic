def primalidad(num):
    num_primo = (int(num) / 2)
    lenght = len(str(num_primo))
    get_decimal = str(num_primo)[lenght-1:]
    if num == '2' or get_decimal != '0' and num != '1':
        return True
    else:
        False

def main():
    number = input('type any number: ')
    if primalidad(number):
        print('Es primo')
    else:
        print("No es primo")

if __name__ == '__main__':
    main()