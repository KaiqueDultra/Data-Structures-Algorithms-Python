def notas():
    quantidade_notas = 0
    soma = 0
    
    while quantidade_notas <= 4:
        nota = int(input("Digite a nota: "))
        quantidade_notas += 1
        soma += nota
    media = soma / quantidade_notas
    print("A média das notas é de: ", media)
    
if __name__ == '__main__':
    notas()