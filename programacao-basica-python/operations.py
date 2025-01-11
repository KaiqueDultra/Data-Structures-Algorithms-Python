def operations():
    valor1 = int(input("Olá, digite o primeiro valor: "))
    valor2 = int(input("Olá, digite o segundo valor: "))

    print(f"O valor da soma de {valor1} e {valor2} é: ", valor1 + valor2)
    print(f"O valor da subtração de {valor1} e {valor2} é: ", valor1 - valor2)
    print(f"O valor da multiplicação de {valor1} e {valor2} é: ", valor1 * valor2)
    print(f"O valor da divisão de {valor1} e {valor2} é: ", valor1 / valor2)

if __name__ == '__main__':
    operations()