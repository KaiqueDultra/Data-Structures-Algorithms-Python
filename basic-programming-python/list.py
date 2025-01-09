def lista():
    lista = []
    soma = 0
    
    for _ in range(1, 6):
        numero = int(input("Digite o valor para ser armazanado na lista: "))
        lista.append(numero)
    print(lista)
    
    for i in lista:
        soma += i
    print(f"A soma de todos os números da lista é de: {soma}")
    
if __name__ == '__main__':
    lista()