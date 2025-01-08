def averages():
    m1 = float(input('Digite a sua nota da matéria M1: '))
    m2 = float(input('Digite a sua nota da matéria M1: '))
    m3 = float(input('Digite a sua nota da matéria M1: '))

    media = (m1 + m2 + m3) / 3

    if media >= 0.0 and media <= 4.0:
        print('Aluno reprovado.')
    elif media >= 4.1 and media <= 6.0:
        print('Aluno de exame')
        nota_exame = float(input('Digite a nota do exame: '))
        if nota_exame > 6.0:
            print('Aluno aprovado')
        else:
            print('Aluno reprovado')
    elif media >= 6.0:
        print('Aluno aprovado')

if __name__ == '__main__':
    averages()