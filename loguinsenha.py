
# Definição do usuário e senha corretos
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "123456"

# Limite de tentativas
tentativas_restantes = 3

print("--- SISTEMA DE LOGIN ---")

# Laço que executa enquanto o usuário tiver tentativas disponíveis
while tentativas_restantes > 0:
    # Pedir dados de acesso
    usuario_digitado = input("\nDigite o nome de usuário: ")
    senha_digitada = input("Digite a senha: ")
    
    # Verificação das credenciais
    if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
        print("Login realizado com sucesso! Bem-vindo ao sistema.")
        break  # Sai do loop imediatamente
    else:
        tentativas_restantes -= 1  # Diminui 1 tentativa
        print("Usuário ou senha incorretos!")
        
        # Informa quantas chances ainda restam, se não for o bloqueio final
        if tentativas_restantes > 0:
            print(f"Você ainda tem {tentativas_restantes} tentativa(s) restante(s).")

# Se o loop acabar e as tentativas zerarem, exibe a mensagem de bloqueio
if tentativas_restantes == 0:
    print("\n[BLOQUEADO] Suas tentativas acabaram. Acesso bloqueado por segurança!")





# Estrutura dos dados usados
# while tentativas_restantes > 0: Garante que o programa vai rodar no máximo 3 vezes, reduzindo o contador a cada erro (tentativas_restantes -= 1).
# break: Interrompe o laço na hora se o usuário acertar o nome e a senha juntos, impedindo que o programa continue pedindo os dados.
# if tentativas_restantes == 0: Uma verificação fora do laço para identificar se o usuário saiu do programa porque esgotou as chances.e










