
# Ano atual para o cálculo da idade
ANO_ATUAL = 2026

# Laço para coletar dados de 12 candidatos
for i in range(1, 13):
    print(f"\n--- Cadastro do Candidato {i} ---")
    
    # Coleta obrigatória do ano de nascimento
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ANO_ATUAL - ano_nascimento
    
    # Decisão para filtrar menores de 18 anos
    if idade < 18:
        print(f"Idade: {idade} anos. Desculpe, você é menor de 18 anos e não pode participar.")
        # O programa pula para o próximo candidato automaticamente
    else:
        print(f"Idade: {idade} anos. Idade permitida! Proseguindo com o cadastro...")
        
        # Coleta dos demais dados apenas para maiores de 18
        nome = input("Digite o nome completo: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        
        print(f"Candidato(a) {nome} cadastrado(a) com sucesso!")





# Estrutura usada para montar os dados de candidatos 
# ANO_ATUAL (2026): Variável fixa para calcular a idade exata de cada candidado e o seu ano de nascimento
# ano_nascimento: Primeiro dado pedido. Ele define se o programa continua ou para ali mesmo, se a idade for menor de 18, não a cadastro .
# Dados condicionais: nome, telefone e email só serão solicitados se a pessoa tiver 18 anos ou mais, se tiver menos cadastro será cancelado devido a menor idade.






