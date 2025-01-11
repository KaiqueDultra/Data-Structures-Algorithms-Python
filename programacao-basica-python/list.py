'''
Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os 
armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para 
somar todos os valores digitados

'''

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