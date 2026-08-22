
#código do produto para cada estado

# Coleta do código do produto
codigo_origem = int(input("Digite o código de origem do produto: "))

# Estrutura de escolha match/case para definir a região baseada na tabela
match codigo_origem:
    case 1:
        regiao = "Sul"
    case 2:
        regiao = "Norte"
    case 3:
        regiao = "Leste"
    case 4:
        regiao = "Oeste"
    case 5 | 6:
        regiao = "Nordeste"
    case 7 | 8 | 9:
        regiao = "Sudeste"
    case 10:
        regiao = "Centro-Oeste"
    case 11:
        regiao = "Noroeste"
    case _:
        regiao = "Importado"

# Exibição do resultado final
print(f"A região de procedência do produto é: {regiao}")



# O programa pede e lê o número digitado pelo usuário através do comando input().

#codigo_origem = int(input("Digite o código de origem do produto: "))







#(match/case): O programa analisa o conteúdo da variável codigo_origem. Ele vai pulando de caso em caso (case) procurando o número correspondente da tabela. O símbolo de barra vertical (|) serve para agrupar múltiplos códigos na mesma região (como no case 5 | 6).

#match codigo_origem:
    #case 1:
        #regiao = "Sul"
    #case 2:
        #regiao = "Norte"
    #case 3:
        #regiao = "Leste"
    #case 4:
        #regiao = "Oeste"
    #case 5 | 6:
        #regiao = "Nordeste"
    #case 7 | 8 | 9:
        #regiao = "Sudeste"
    #case 10:
        #regiao = "Centro-Oeste"
    #case 11:
        #regiao = "Noroeste"
    #case _:
        #regiao = "Importado"


 #terminal imprime a região encontrada de forma direta.

#print(f"A região de procedência do produto é: {regiao}")









