import random

# Lista de profissionais disponíveis para a escala de atendimento
garcoms = ["Paulo", "Lucas", "Maria", "Ana", "Luiz", "Carolina", "Gabriel", "Fabiana", "Eloan", "Roberta"]

# Criando o restaurante com 10 mesas inicialmente vazias (None)
mesa = [None] * 10 

# ========================================================================================================
def vincular_garcom_mesa(numero_mesa, nome_garcom):
    """
    Função usada para vincular um garçom a uma mesa específica.
    """
    # 2. VALIDAÇÃO DOS PARÂMETROS
    if numero_mesa is None or nome_garcom is None:
        return "Erro: Falta enviar o número da mesa ou o nome do garçom."  
         
    if type(numero_mesa) is not int or type(nome_garcom) is not str:
        return "Erro: Mesa deve ser número inteiro e Garçom deve ser texto."

    # 3. TRATAMENTO DE ERROS E REGRAS DE NEGÓCIO
    if numero_mesa < 1 or numero_mesa > len(mesa):
        return f"Erro: A mesa {numero_mesa} não existe no restaurante."

    if nome_garcom not in garcoms:
        return f"Erro: O garçom {nome_garcom} não trabalha aqui."

    # 4. IMPLEMENTAÇÃO DA FUNÇÃO (LÓGICA PRINCIPAL)
    posicao_lista = numero_mesa - 1
    mesa[posicao_lista] = nome_garcom
    return f"Sucesso: Garçom {nome_garcom} vinculado à mesa {numero_mesa}."


# ==============================================================================
# Sorteia os garçons que estão disponíveis para atender as mesas
comparecer_mesa = random.randint(1, 10)  
garcom_sorteado = random.choice(garcoms)

# Exibe os dados do chamado na tela
print("--- CHAMADO DE ATENDIMENTO ---")
print(f"Mesa que chamou: Mesa {comparecer_mesa}")
print(f"Garçom escalado: {garcom_sorteado}")
print("------------------------GARÇOM INDO A MESA COM SEU PEDIDO--------------------")

# Executa a função para vincular o garçom na lista de mesas (Apenas processa internamente)
resultado_do_sistema = vincular_garcom_mesa(comparecer_mesa, garcom_sorteado)
print(resultado_do_sistema)


