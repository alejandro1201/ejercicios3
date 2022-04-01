print("Digite tres valores para calcular el minimo")
valor1 = int(input("primer valor: "))
valor2 = int(input("segundo valor: "))
valor3 = int(input("tercer valor: "))

if valor1 < valor2:
    if valor1 < valor3:
        minimo_valor = valor1
    else:
        minimo_valor = valor3
elif valor2 < valor3:
    minimo_valor = valor2
else:
    minimo_valor = valor3

print("El numero minimo es: ", minimo_valor)
