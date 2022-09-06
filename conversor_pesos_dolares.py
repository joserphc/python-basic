pesos = input("¿Cuántos pesos tienes:? ")
pesos = float(pesos)
valor_pesos_a_dolares = 0.00022
resultado_conversion = pesos * valor_pesos_a_dolares
resultado_conversion = round(resultado_conversion, 4)
resultado_conversion = str(resultado_conversion)
print("Usted tiene $" + resultado_conversion + " dólares")