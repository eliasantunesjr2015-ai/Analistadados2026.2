# Média dos alunos5


# Coleta das notas do estudante
nota1 = float(input("Digite a nota da 1ª Avaliação: "))
nota2 = float(input("Digite a nota da 2ª Avaliação: "))
nota_optativa = float(input("Digite a nota da Optativa (ou -1 se não fez): "))

# Processamento: Verificação da substituição da nota mais baixa
if nota_optativa != -1:
    # Se a nota 1 for a menor e a optativa for melhor, substitui a nota 1
    if nota1 < nota2 and nota_optativa > nota1:
        nota1 = nota_optativa
    # Se a nota 2 for a menor e a optativa for melhor, substitui a nota 2
    elif nota2 <= nota1 and nota_optativa > nota2:
        nota2 = nota_optativa

# Cálculo da média semestral com as notas finais
media_semestre = (nota1 + nota2) / 2

print(f"\nMédia final obtida: {media_semestre}")

# Estrutura de decisão em cadeia para definir a situação do estudante
if media_semestre >= 6.0:
    situacao = "Aprovado"
elif media_semestre < 3.0:
    situacao = "Reprovado"
else:
    situacao = "Em Recuperação"

print(f"Situação do estudante: {situacao}")










 #O programa recebe a nota1, nota2 e a nota_optativa. Se o estudante não fez a prova extra, o valor digitado deve ser -1.

#nota1 = float(input("Digite a nota da 1ª Avaliação: "))
#nota2 = float(input("Digite a nota da 2ª Avaliação: "))
#nota_optativa = float(input("Digite a nota da Optativa (ou -1 se não fez): "))







 #Primeiro, o programa confere se a optativa é diferente de -1. Se for, ele usa um if/elif interno para descobrir qual das duas primeiras notas foi a mais baixa e a substitui pela nota da optativa (caso a optativa seja maior). Depois, soma as duas notas finais e divide por 2 para achar a media_semestre.

#if nota_optativa != -1:
    # Se a nota 1 for a menor e a optativa for melhor, substitui a nota 1
    #if nota1 < nota2 and nota_optativa > nota1:
        #nota1 = nota_optativa
    # Se a nota 2 for a menor e a optativa for melhor, substitui a nota 2
    #elif nota2 <= nota1 and nota_optativa > nota2:
        #nota2 = nota_optativa



#Cálculo da Média: A linha media_semestre = (nota1 + nota2) / 2 soma as duas notas finais do aluno (já considerando se a optativa substituiu a menor nota ou não) e divide o resultado por 2. Os parênteses servem para avisar o Python que ele deve fazer a soma primeiro e depois a divisão.

#media_semestre = (nota1 + nota2) / 2

#print(f"\nMédia final obtida: {media_semestre}")











#(if/elif/else): Ele avalia a média final ou igual a 6 é Aprovado, abaixo de 3 é Reprovado, e qualquer valor intermediário cai no else como Em Recuperação.


#if media_semestre >= 6.0:
    #situacao = "Aprovado"
#elif media_semestre < 3.0:
    #situacao = "Reprovado"
#else:
    #situacao = "Em Recuperação"







#Exibe no terminal a média calculada e o status final do aluno.

#print(f"Situação do estudante: {situacao}")












