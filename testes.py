import pandas as pd
from sqlalchemy import create_engine

# --- PASSO A: ANÁLISE ESTATÍSTICA (PANDAS) ---
print("=== Realizando Análise Estatística no CSV ===")
# Substitua pelo caminho real do seu arquivo CSV
df = pd.read_csv("seu_arquivo_funcionarios.csv") 

# Exibe informações gerais e estatísticas pedidas no projeto
print(df.info())
print("\nResumo Estatístico dos Salários:")
print(df['salario'].describe()) 
print("-" * 50)


# --- PASSO B: ENVIAR DADOS PARA O MYSQL ---
print("=== Iniciando Ingestão de Dados no Banco ===")

# Defina as credenciais do seu MySQL local
usuario = "root"
senha = "sua_senha_aqui"
host = "localhost"
banco = "nome_do_seu_banco"

# Cria a engine de conexão via SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{senha}@{host}/{banco}")

# Envia os dados do DataFrame para a tabela do MySQL
# Certifique-se de que 'nome_da_tabela' é o mesmo nome usado nas suas 5 consultas
df.to_sql(name='nome_da_sua_tabela', con=engine, if_exists='append', index=False)

print("Dados inseridos com sucesso! Agora executando as consultas...")
print("-" * 50)

# --- (Daqui para baixo continua o seu código atual das 5 consultas) ---






