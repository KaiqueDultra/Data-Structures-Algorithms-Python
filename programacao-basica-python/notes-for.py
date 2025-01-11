def notas():
    quantidade_notas = 0
    soma = 0
    
    for _ in range(1, 6):
        notas = int(input("Digite o valor da nota: "))
        quantidade_notas += 1
        soma += notas
        
    media = soma / quantidade_notas
    print(media)
    
if __name__ == '__main__':
    notas()