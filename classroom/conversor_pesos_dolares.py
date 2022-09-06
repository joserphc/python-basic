def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos +" tienes:? ")
    pesos = float(pesos)
    resultado_conversion = pesos / valor_dolar
    resultado_conversion = round(resultado_conversion, 2)
    resultado_conversion = str(resultado_conversion)
    print("Usted tiene $" + resultado_conversion + " dólares")

menu_bienvenida = """
Bienvenido al conversor de monedas 💰

Eliga entre estás opciones:

1 - pesos argentinos
2 - pesos colombianos
3 - pesos mexicanos

Usted eligio:
"""

opcion = input(menu_bienvenida)

if opcion == '1':
    conversor("argentinos", 140.58)
elif opcion == '2':
    conversor("colombianos", 4478.67)
elif opcion == '3':
    conversor("mexicanos", 20.15)
else:
    print("No seleccionastes ninguna opción")