
USE projeto_sql;

-- ===========================================================================
-- CRIAÇÃO DAS TABELAS
-- ===========================================================================
-- TABELA 1: Contratacao Localizar
DROP TABLE IF EXISTS contratacao_localizar;
CREATE TABLE contratacao_localizar (
    ID INT PRIMARY KEY,
    Genero VARCHAR(50) NOT NULL,
    Cargo VARCHAR(150) NOT NULL,
    Salario DECIMAL(10,2) NOT NULL,
    Data_Contratacao DATE NOT NULL
);


-- TABELA 2: desligamentos funcionarios
DROP TABLE IF EXISTS desligamentos_funcionarios;
CREATE TABLE desligamentos_funcionarios (
    ID INT PRIMARY KEY,
    Genero VARCHAR(50) NOT NULL,
    Motivo_Desligamento INT NOT NULL,
    Data_Desligamento DECIMAL(5,2) NOT NULL
);

-- TABELA 3: Contratacao por regiao 
DROP TABLE IF EXISTS contratacao_regioes;
CREATE TABLE contratacao_regioes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Regiao VARCHAR(100) NOT NULL,
    Funcao INT NOT NULL,
    Genero VARCHAR(50) NOT NULL
);

-- TABELA 4: desligamentos por regiao
DROP TABLE IF EXISTS desligamentos_por_regiao;
CREATE TABLE desligamentos_por_regiao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Genero VARCHAR(50) NOT NULL,
    Funcao INT NOT NULL,
    Regiao VARCHAR(100) NOT NULL,
    Motivo_Desligamento INT NOT NULL
);

-- TABELA 5: Contratacao faixa etaria
DROP TABLE IF EXISTS contratacao_faixaetaria;
CREATE TABLE contratacao_faixaetaria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Faixa_Etaria VARCHAR(50) NOT NULL,
    genero INT NOT NULL,
    Funcao INT NOT NULL,
    Regiao INT NOT NULL
);

-- TABELA 6: desligamento faixa etaria
DROP TABLE IF EXISTS desligamento_faixaetaria;
CREATE TABLE desligamento_faixaetaria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Faixa_Etaria VARCHAR(50) NOT NULL,
    genero INT NOT NULL,
    funcao DECIMAL NOT NULL
);

-- EXIBIR TABELAS CRIADAS
SHOW TABLES;

-- VALIDAR QUANTIDADE DE REGISTROS 
SELECT 'contratacao_localizar' AS tabela, COUNT(*) AS total FROM projeto_sql.contratacao_localizar UNION ALL
SELECT 'desligamentos_funcionarios', COUNT(*) FROM projeto_sql.desligamentos_funcionarios UNION ALL
SELECT 'contratacao_regioes', COUNT(*) FROM projeto_sql.contratacao_regioes UNION ALL
SELECT 'desligamentos_por_regiao', COUNT(*) FROM projeto_sql.desligamentos_por_regiao UNION ALL
SELECT 'contratacao_faixaetaria', COUNT(*) FROM projeto_sql.contratacao_faixaetaria UNION ALL
SELECT 'desligamento_faixaetaria', COUNT(*) FROM projeto_sql.desligamento_faixaetaria;



-- ===========================================================================
-- AS 6 CONSULTAS ESTRATÉGICAS FEITAS PELO RH, JUNTO AO FINANCEIRO E COMERCIAL
-- ===========================================================================

-- CONSULTA 1: Perfil Geral de Contratação por Cargo, Salário, Gênero e data de contratação
-- Objetivo: Alimentar gráficos de distribuição de cargos, gêneros e salários detalhados.
SELECT 
    Genero, 
    Cargo, 
    Salario,
    Data_Contratacao
FROM projeto_sql.contratacao_localizar;


-- CONSULTA 2: Análise Demográfica de Desligamentos por Gênero
-- Objetivo: Exibir a proporção e volume de saídas divididos por gênero.
SELECT 
    Genero, 
    Motivo_Desligamento, 
    Data_Desligamento 
FROM projeto_sql.desligamentos_funcionarios;


-- CONSULTA 3: Balanço de Movimentação por contratação por região
-- Objetivo: Comparar contratações por região em um gráfico de colunas agrupadas.
SELECT 
    Regiao, 
    Funcao,
    Genero
FROM projeto_sql.contratacao_regioes;


-- CONSULTA 4: Desligamentos por região
-- Objetivo: Demonstrar os desligamentos por região.
SELECT 
    Genero, 
    Funcao,
    Regiao,
    Motivo_Desligamento
FROM projeto_sql.desligamentos_por_regiao;


-- CONSULTA 5: Mapeamento de contratação por faixa etária
-- Objetivo: Identificar as contratações feitas por faixa etária e suas funções.
SELECT 
    Faixa_Etaria, 
    Genero,
    Funcao,
    Regiao
FROM projeto_sql.contratacao_faixaetaria;


-- CONSULTA 6: Mapeamento de desligamento por faixa etária
-- Objetivo: Identificar os desligamentos por faixa etária e suas funções.
SELECT 
    Faixa_Etaria,
    genero,
    funcao
FROM projeto_sql.desligamento_faixaetaria;
