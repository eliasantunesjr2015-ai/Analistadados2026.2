
# Laço para repetir a lógica para 10 estudantes
for i in range(1, 11):
    print(f"\n--- Cadastro do {i}º Estudante ---")
    
    # Leitura do nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Leitura das notas do aluno
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    
    # Cálculo da média aritmética
    media = (nota1 + nota2) / 2
    
    # Exibição do resultado
    print(f"\nAluno(a): {nome}")
    print(f"Média: {media:.2f}")
    
    # Verificação do status do aluno
    if media >= 7.0:
        print("Status: Aprovado")
    elif media >= 5.0:
        print("Status: Recuperação")
    else:
        print("Status: Reprovado")






# Estrutura montada para exibir os dados 
#. Usei o input para ("Digita o nome do aluno: ") 
#float(input(...)): Recebe as notas e o nome de cada aluno e as transforma em números decimais.
# if/elif/else: Avalia em qual situação o aluno se encaixa de acordo com a média calculada








