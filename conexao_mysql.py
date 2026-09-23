
import mysql.connector
from mysql.connector import Error

def conectar_banco():
    """Estabelece a conexão com o banco de dados MySQL"""
    try:
        conexao = mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='270291elias',   
            database='projeto_sql'    
        )
        if conexao.is_connected():
            print(" Conexão ao MySQL realizada com sucesso!\n")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def executar_consulta(conexao, titulo, query):
    """Executa uma consulta SQL e exibe os resultados formatados"""
    cursor = conexao.cursor()
    try:
        cursor.execute(query)
        resultados = cursor.fetchall()
        
        # Obtém os nomes das colunas
        colunas = [desc[0] for desc in cursor.description]
        
        print(f"=== {titulo} ===")
        # Exibe o cabeçalho das colunas
        print(" | ".join(colunas))
        print("-" * 50)
        
        # Exibe as linhas de dados
        for linha in resultados:
            print(" | ".join(str(item) for item in linha))
        print(f"Total de registros encontrados: {len(resultados)}\n")
        
    except Error as e:
        print(f"Erro ao executar consulta: {e}\n")
    finally:
        cursor.close()

def main():
    conexao = conectar_banco()
    if conexao:
        # Consulta 1. Seleção simples (Trazer tudo)
        q1 = "SELECT * FROM funcionarios;"
        executar_consulta(conexao, "Consulta 1: Todos os Funcionários", q1)

        # Consulta 2. Filtro específico (Apenas funcionárias do gênero feminino)
        q2 = "SELECT nome_completo, cargo, salario FROM funcionarios WHERE genero = 'Feminino';"
        executar_consulta(conexao, "Consulta 2: Funcionárias do Gênero Feminino", q2)

        # Consulta 3. Ordenação e Operadores (Salários maiores que R$ 5.000,00 em ordem decrescente)
        q3 = "SELECT nome_completo, cargo, salario FROM funcionarios WHERE salario > 5000.00 ORDER BY salario DESC;"
        executar_consulta(conexao, "Consulta 3: Salários Maiores que R$ 5.000,00 (Ordem Decrescente)", q3)

        # Consulta 4. Funções Agregadas (Média salarial e total da folha de pagamento)
        q4 = "SELECT AVG(salario) AS media_salarial, SUM(salario) AS total_folha_pagamento FROM funcionarios;"
        executar_consulta(conexao, "Consulta 4: Média Salarial e Total da Folha", q4)

        # Consulta 5. Agrupamento com funções (Quantidade de funcionários e média salarial por cargo)
        q5 = "SELECT cargo, COUNT(*) AS qtd_funcionarios, AVG(salario) AS media_salario_cargo FROM funcionarios GROUP BY cargo;"
        executar_consulta(conexao, "Consulta 5: Resumo de Funcionários e Média Salarial por Cargo", q5)

        # Fecha a conexão com o banco
        conexao.close()
        print("Conexão com o MySQL encerrada.")

if __name__ == '__main__':
    main()
