#Title
print("Algoritmo para clientes de ACNÉ")
#Variables
antiguedad = int(input("Por favor introduzca la cantidad de años: "))
valor_compra = int(input("Digite el valor de su compra: "))
descuento = valor_compra * 0.25
descuento_mayorista = valor_compra * 0.20
descuento_minorista = valor_compra * 0.18
descuento_ocasional = valor_compra * 0.10
valor_a_pagar = valor_compra - descuento
valor_a_pagar_mayorista = valor_compra - descuento_mayorista
valor_a_pagar_minorista = valor_compra - descuento_minorista
valor_a_pagar_ocasional = valor_compra - descuento_ocasional
#Conditionals
if antiguedad > 2 and antiguedad < 5 and valor_compra > 2000000 :
    print("Tipo de cliente: Mayorista")
    print("El valor de tu compra es: ", (valor_compra))
    print("Tienes un descuento del 25%, así que el valor a pagar es: "),print(int(valor_a_pagar))    
elif antiguedad <= 2 and valor_compra >= 1500000 and valor_compra <= 2000000 :
    print("Tipo de cliente: Mayorista")
    print("El valor de tu compra es: ", (valor_compra))
    print("Tienes un descuento del 20%, así que el valor a pagar es: "),print(int(valor_a_pagar_mayorista))
elif antiguedad > 5 and valor_compra > 2000000 :
    print("Tipo de cliente: Minorista")
    print("El valor de tu compra es: ", (valor_compra))
    print("Tienes un descuanto del 18%, así que el valor a pagar es: "),print(int(valor_a_pagar_minorista))
elif antiguedad < 2 and valor_compra > 2000000 :
    print("Tipo de cliente: Ocasional")
    print("El valor de tu compra es: ", (valor_compra))
    print("Tienes un descuento del 10%, así que el valor a pagar es: "), print(int(valor_a_pagar_ocasional))
else:
    print("Sus datos no coinciden con el algoritmo")
