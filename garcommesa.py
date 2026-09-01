
import random
# Alterado o nome da variável e adicionado estados de 'Livre' e 'Ocupada' para teste
status_mesa = ["Livre", "Ocupada", "Livre", "Livre", "Ocupada", "Livre", "Livre", "Livre", "Livre", "Livre"]

# Lista de profissionais disponíveis para a escala de atendimento
garcoms = ["Paulo", "Lucas", "Maria", "Ana", "Luiz", "Carolina", "Gabriel", "Fabiana", "Eloan", "Roberta"]

# ========================================================================================================
def vincular_garcom_mesa(numero_mesa, nome_garcom):
    """
    Função usada para vincular um garçom a uma mesa especifica, garantindo que a mesa esteja disponível e que o garcom esteja ativo no sistema. Para o atendimento ao cliente, na mesa solicitada.
    """
    #2. VALIDAÇÃO DOS PARÂMETROS
    if numero_mesa is None or nome_garcom is None:
        return "Erro: Falta enviar o número da mesa ou o nome do garçom."  
         
    if type(numero_mesa) is not int or type(nome_garcom) is not str:
        return "Erro: Mesa deve ser número inteiro e Garçom deve ser texto."

    # 3. TRATAMENTO DE ERROS E REGRAS DE NEGÓCIO
    if numero_mesa < 1 or numero_mesa > len(status_mesa):
        return f"Erro: A mesa {numero_mesa} não existe no restaurante."

    if nome_garcom not in garcoms:
        return f"Erro: O garçom {nome_garcom} não trabalha aqui."

    posicao_lista = numero_mesa - 1

    # Nova regra adicionada: Verifica se a mesa sorteada já está ocupada
    if status_mesa[posicao_lista] == "Ocupada":
        return f"Erro: A mesa {numero_mesa} já está ocupada."

    # 4. IMPLEMENTAÇÃO DA FUNÇÃO (LÓGICA PRINCIPAL)
    status_mesa[posicao_lista] = "Ocupada"
    return f"Sucesso: Garçom {nome_garcom} vinculado à mesa {numero_mesa}."


# ==============================================================================
# Sorteia os garçons que estão disponíveis para atender as mesas que foram solicitadas pelo sistema.
comparecer_mesa = random.randint(1, 10)  
garcom_sorteado = random.choice(garcoms)

# Exibe os dados de forma que o garçom e o cliente possam olhar e te uma boa localização através de uma tela de atendimento onde ali, diz a mesa que solicitou o atendimento e o garçom disponível para atender.
print("--- CHAMADO DE ATENDIMENTO  ---")
print(f"Mesa que chamou: Mesa {comparecer_mesa}")
print(f"Garçom escalado: {garcom_sorteado}")
print("------------------------GARÇOM INDO A MESA COM SEU PEDIDO--------------------")

# Função criada para vincular o garçom sorteado á mesa que solicitou o atendimento.
resultado_do_sistema = vincular_garcom_mesa(comparecer_mesa, garcom_sorteado)
print(resultado_do_sistema)




#FUNCÕES USADAS PARA VINCULAR GARÇOM A UMA MESA :

        # IMPORT RANDOM SERVIU PARA SER USADO, COMO SORTEIO DE GARÇOM A MESA, "MESAS LIVRES" OU SE A "MESA TIVER OCUPADA" MOSTRA NO SISTEMA POR QUE AINDA CONSTA O CLIENTE NA MESA E "GARÇONS DISPONÍVEIS" PARA O ATENDIMENTO .
        # DEF FOI USADO PARA VINCULAR O GARÇOM A MESA SOLICITADA PELO SISTEMA, E O SISTEMA ME DIZ SE ESSE GARÇOM CHEGOU A MESA, SE NÃO OUTRO GARÇOM, IRÁ ATENDER MESA SOLICITADA.
        # RANDOM. RANDINT USADA FUNÇÃO PARA SORTEAR A MESA QUE FOI SOLICITADA PELO SISTEMA .
        # RANDOM. CHOICE USADA FUNÇAO PARA SORTEAR O GARÇOM DISPONÍVEL NO SISTEMA PARA ATENDIMENTO .
        # USEI PRINTS UM PARA EXIBIR O CHAMADO DE ATENDIMENTO E OUTRO, PARA DIZER A MESA QUE CHAMOU E OUTRO PARA DIZER O GARÇOM QUE IRÁ A MESA SOLICITADA.

        #========== PRIMEIRO ABRIU CHAMADO DE ATENDIMENTO, DEPOIS DESSE CHAMADO, O GARÇOM FOI A MESA COM O PEDIDO DO CLIENTE.

                        # FUNÇÃO PRINT AQUI FUI USADA, PARA VINCULAR O GARÇOM A MESA SOLICITADA, E MOSTRA O RESULTADO NO TERMINAL.


