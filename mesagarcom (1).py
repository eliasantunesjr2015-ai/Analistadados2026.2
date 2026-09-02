import random

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

# Sorteia se o cliente desistiu ou não.
cliente_desistiu = random.choice([True, False])

# Executa a sua função interna e guarda a resposta
resultado_do_sistema = vincular_garcom_mesa(comparecer_mesa, garcom_sorteado)


# 📱 1. VISÃO DO GARÇOM (Interface de atendimento rápido,para ele saber qual mesa solicitou seu atendimento).
print("\n📱 [ VISÃO INTERFACE: GARÇOM ]")
print("--- CHAMADO DE ATENDIMENTO  ---")
print(f"Mesa que chamou: Mesa {comparecer_mesa}")
print(f"Garçom escalado: {garcom_sorteado}")
print("-----------------------------------------------------------------------------")

# CASO 1: Deu sucesso na função E o cliente NÃO desistiu
if "Sucesso" in resultado_do_sistema and not cliente_desistiu:
    print(f"✅ Pedido Confirmado! {garcom_sorteado} está indo levar o pedido até a Mesa {comparecer_mesa}.")

# CASO 2: Deu sucesso no sistema, mas o cliente desistiu na hora H e foi embora
elif "Sucesso" in resultado_do_sistema and cliente_desistiu:
    # Como ele desistiu, precisamos liberar a mesa na lista novamente
    status_mesa[comparecer_mesa - 1] = "Livre"
    print(f"⚠️ Alerta {garcom_sorteado}! O garçom foi até a mesa, mas o cliente desistiu e foi embora.")
    print(f"   Status da Operação: Atendimento cancelado por desistência.")

# CASO 3: Deu erro na função (Ex: Mesa Ocupada)
else:
    print(f"❌ Alerta {garcom_sorteado}! Não foi possível lançar o pedido.")
    print(f"   Diagnóstico do Sistema: {resultado_do_sistema}")

# ESSE ERRO DO SISTEMA FOI UM BUG UMA FALHA NO SISTEMA, POIS DIZIA QUE A MESA TAVA LIVRE, O GARÇOM IA A MESA E ELA ESTAVA OCUPADA .



#==================================================================================
        #CRIEI 3 CASOS PARA TESTAR O SISTEMA, EM SITUAÇÕES DIFERENTES, UMA FOI DE SUCESSO, O CLIENTE NÃO DESISTIU. E A OUTRA MOSTROU QUE O CLIENTE DESISTIU. E OUTRO CASO MOSTROU A MESA OCUPADA.


