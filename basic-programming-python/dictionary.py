def dicionario():
    dicionario_notas = {}
    soma = 0
    
    for _ in range(1, 4):
        nome = input("Informe o seu nome: ")
        notas = int(input('Informe a sua nota: '))
        dicionario_notas[nome] = notas
    print("-------------------------")
    print(dicionario_notas)
    
    for _, notas in dicionario_notas.items():
        soma += notas
        media = soma / 3
    print("-------------------------")   
    print(f"A média de todas as notas informadas é de: {media}")
        
        
if __name__ == '__main__':
    dicionario()