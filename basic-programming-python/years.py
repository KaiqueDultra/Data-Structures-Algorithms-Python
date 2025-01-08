def idade():
    idade = int(input("Olá, nos informe a sua idade: "))

    if idade >= 0 and idade <= 12:
        print("Classificação: Criança.")
    elif idade > 12 and idade <= 17:
        print("Classificação: Adolescente.")
    elif idade >= 18:
        print("Classificação: Adulto.")
    else:
        print("Idade invalida.")

if __name__ == '__main__':
    idade()