 USE projeto_sql;

-- TABELA 1: Contratacoes Localiza
DROP TABLE IF EXISTS Contratacoes_localiza;
CREATE TABLE projeto_sql.contratacoes_localiza (
ID INT PRIMARY KEY,
Nome_Completo VARCHAR(255) NOT NULL,
Genero VARCHAR(50) NOT NULL,
Cargo VARCHAR(150) NOT NULL,
Salario DECIMAL(10,2) NOT NULL
);

-- TABELA 2: Desligamentos funcionarios
DROP TABLE IF EXISTS Desligamentos_funcionarios;
CREATE TABLE Desligamentos_funcionarios (
ID INT PRIMARY KEY,
Genero VARCHAR(50) NOT NULL,
Desligamentos INT NOT NULL,
Taxa_Desligamento DECIMAL(5,2) NOT NULL
);

-- TABELA 3: Contratacoes por regiao 
DROP TABLE IF EXISTS contratacoes_regioes;
CREATE TABLE contratacoes_regioes (
id INT AUTO_INCREMENT PRIMARY KEY,
Regiao VARCHAR(100) NOT NULL,
Numero_Total_Contratacoes INT NOT NULL,
Taxa_Contratacao DECIMAL(5,2) NOT NULL
);

-- TABELA 4: Desligamento por regiao
DROP TABLE IF EXISTS desligamento_regiao;
CREATE TABLE desligamento_regiao (
id INT AUTO_INCREMENT PRIMARY KEY,
Regiao VARCHAR(100) NOT NULL,
Desligamentos INT NOT NULL,
Taxa_Desligamento DECIMAL(5,2) NOT NULL
);

-- TABELA 5: Contratacoes faixa etaria
DROP TABLE IF EXISTS contratacoes_faixaetaria;
CREATE TABLE contratacoes_faixaetaria (
id INT AUTO_INCREMENT PRIMARY KEY,
Faixa_Etaria VARCHAR(50) NOT NULL,
Numero_Total_Contratacoes INT NOT NULL,
Taxa_Contratacao DECIMAL(5,2) NOT NULL
);

-- TABELA 6: Desligamento faixa etaria
DROP TABLE IF EXISTS desligamento_faixaetaria;
CREATE TABLE desligamento_faixaetaria (
id INT AUTO_INCREMENT PRIMARY KEY,
Faixa_Etaria VARCHAR(50) NOT NULL,
Deskigamentos INT NOT NULL,
Taxa_Desligamento DECIMAL(5,2) NOT NULL
);

SHOW TABLES;

SELECT 'Contratacoes_localiza' as tabela, COUNT(*) as total FROM projeto_sql.contratacoes_localiza UNION ALL
SELECT 'desligamentos_funcionarios', COUNT(*) FROM projeto_sql.desligamentos_funcionarios UNION ALL
SELECT 'contratacoes_regioes', COUNT(*) FROM projeto_sql.contratacoes_regioes UNION ALL
SELECT 'desligamento_regiao', COUNT(*) FROM projeto_sql.desligamento_regiao UNION ALL
SELECT 'contratacoes_faixaetaria', COUNT(*) FROM projeto_sql.contratacoes_faixaetaria UNION ALL
SELECT 'desligamento_faixaetaria', COUNT(*) FROM projeto_sql.desligamento_faixaetaria;


-- ===========================================================================
-- AS 5 CONSULTAS ESTRATÉGICAS FEITAS PELO RH, JUNTO AO FINANCEIRO E COMERCIAL
-- ===========================================================================

-- CONSULTA 1: Perfil Geral de Contratações por Cargo e Gênero (Mapeia os 9.156 registros)
-- Objetivo: Alimentar gráficos de distribuição de cargos, gêneros e salários.
SELECT 
    Nome_Completo,
    Genero, 
    Cargo, 
    Salario 
FROM projeto_sql.contratacoes_localiza;


-- CONSULTA 2: Análise Demográfica de Desligamentos por Gênero
-- Objetivo: Exibir a proporção e volume de saídas divididos por gênero.
SELECT 
    Genero, 
    Desligamentos, 
    Taxa_Desligamento 
FROM projeto_sql.desligamentos_funcionarios;


-- CONSULTA 3: Balanço de Movimentação por Região Geográfica (Contratações vs Desligamentos)
-- Objetivo: Comparar entradas e saídas por região em um gráfico de colunas agrupadas.
SELECT 
    c.Regiao, 
    c.Numero_Total_Contratacoes, 
    d.Desligamentos AS Total_Desligamentos
FROM projeto_sql.contratacoes_regioes c
INNER JOIN projeto_sql.desligamento_regiao d ON c.Regiao = d.Regiao;


-- CONSULTA 4: Distribuição de Novas Contratações por Faixa Etária
-- Objetivo: Demonstrar o volume e a taxa de atração de novos talentos por idade.
SELECT 
    Faixa_Etaria, 
    Numero_Total_Contratacoes, 
    Taxa_Contratacao 
FROM projeto_sql.contratacoes_faixaetaria;


-- CONSULTA 5: Mapeamento de Desligamentos por Faixa Etária
-- Objetivo: Identificar qual grupo geracional possui o maior índice de turnover.
SELECT 
    Faixa_Etaria, 
    Deskigamentos AS Total_Desligamentos, 
    Taxa_Desligamento 
FROM projeto_sql.desligamento_faixaetaria;






