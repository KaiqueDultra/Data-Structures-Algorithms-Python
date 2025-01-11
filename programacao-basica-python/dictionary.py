'''
Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura 
dos valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição 
para somar todas as notas e retornar a média.

'''

def dicionario():
    dicionario_notas = {}
    soma = 0
    
    for _ in range(1, 4):
        nome = input("Informe o seu nome: ")
        notas = int(input('Informe a sua nota: '))
        dicionario_notas[nome] = notas
    print("-------------------------")
    print(dicionario_notas)
    
    for notas in dicionario_notas.values():
        soma += notas
        media = soma / 3
    print("-------------------------")   
    print(f"A média de todas as notas informadas é de: {media}")
        
        
if __name__ == '__main__':
    dicionario()