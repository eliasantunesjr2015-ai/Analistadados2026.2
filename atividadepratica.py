import pandas as pd

# 1. Carrega as abas necessárias diretamente do arquivo Excel
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativos = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')


print("1. Quais são as máximas e mínimas de operação de compra e venda?")
#  print usado para mim dizer na tabela quem tem a maior compra e venda, e quem vendeu menos e comprou menos


resultado_operacoes = df_transacoes.groupby('operacao')['preco'].agg(['min', 'max'])
print(resultado_operacoes)
print('-' * 20)


print("2. Qual CNPJ tem o ativo de maior valor?")
# para dizer qual CNPJ, que mas investiu

# Para sabe na tabela qual CNPJ ativo que teve mas transações "id ativo"
df_completo = pd.merge(df_transacoes, df_ativos, on='id_ativo')

# Localiza a linha com o maior preço 
maior_ativo = df_completo.loc[df_completo['preco'].idxmax()]

print(f"CNPJ: {maior_ativo['cnpj']}")
print(f"Preço do Ativo: R$ {maior_ativo['preco']:.2f}")
print('-' * 20)

print(". Qual CNPJ tem o ativo de menor valor?")


# localizar a linha com menor preço
menor_ativo = df_completo.loc[df_completo['preco'].idxmin()]

print(f"CNPJ: {menor_ativo['cnpj']}")
print(f"Preço do Ativo: R$ {menor_ativo['preco']:.2f}")
print('-' * 20)


print("3. Qual valor total em transações de cada participante?")

# Lógica direta: calcula e agrupa os valores
participantes_movimentacao = (df_transacoes['quantidade'] * df_transacoes['preco']).groupby(df_transacoes['id_participante']).sum()

print(participantes_movimentacao)
print('-' * 20)


