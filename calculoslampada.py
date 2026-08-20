# Cálculos de lâmpadas

# Fator fixo de iluminação por metro quadrado
CONSUMO_M2 = 3

# Coleta das especificações do ambiente e equipamento
capacidade_lampada = int(input("Qual a potência de cada lâmpada (W)? "))
medida_largura = int(input("Digite a largura da peça (m): "))
medida_comprimento = int(input("Digite o comprimento da peça (m): "))

# Cálculo da superfície e da carga de iluminação necessária
total_m2 = medida_largura * medida_comprimento
carga_necessaria = total_m2 * CONSUMO_M2

print("Espaço total medido:", total_m2, "m².")
print("Necessidade total de iluminação:", carga_necessaria, "Watts.")

# Determinação do total de unidades usando a estrutura if/elif/else
if carga_necessaria <= capacidade_lampada:
    unidades = 1
elif carga_necessaria <= (capacidade_lampada * 2):
    unidades = 2
elif carga_necessaria <= (capacidade_lampada * 3):
    unidades = 3
elif carga_necessaria <= (capacidade_lampada * 4):
    unidades = 4
elif carga_necessaria <= (capacidade_lampada * 5):
    unidades = 5
elif carga_necessaria <= (capacidade_lampada * 6):
    unidades = 6
else:
    unidades = "Acima de 6 unidades (ambiente excessivamente grande)"

print(f"Total de lâmpadas que devem ser instaladas: {unidades}")


# explicação de como usei os dados :

# O programa recebe a potência da lâmpada, a largura e o comprimento através do comando input().

#capacidade_lampada = int(input("Qual a potência de cada lâmpada (W)? "))
#medida_largura = int(input("Digite a largura da peça (m): "))
#medida_comprimento = int(input("Digite o comprimento da peça (m): "))

#Processamento: Ele multiplica largura por comprimento para achar a área (total_m2) e multiplica o resultado por 3 para achar os Watts totais (carga_necessaria).

#total_m2 = medida_largura * medida_comprimento
#carga_necessaria = total_m2 * CONSUMO_M2

#print("Espaço total medido:", total_m2, "m².")
#print("Necessidade total de iluminação:", carga_necessaria, "Watts.")

#(if/elif/else): Ele testa se a carga total cabe em 1 lâmpada, 2 lâmpadas, 3 lâmpadas (e assim por diante), multiplicando a potência individual até o limite de 6 unidades.

#if carga_necessaria <= capacidade_lampada:
    #unidades = 1
#elif carga_necessaria <= (capacidade_lampada * 2):
    #unidades = 2
#elif carga_necessaria <= (capacidade_lampada * 3):
    #unidades = 3
#elif carga_necessaria <= (capacidade_lampada * 4):
    #unidades = 4
#elif carga_necessaria <= (capacidade_lampada * 5):
    #unidades = 5
#elif carga_necessaria <= (capacidade_lampada * 6):
    #unidades = 6
#else:
    #unidades = "Acima de 6 unidades (ambiente excessivamente grande)"

# O programa exibe na tela o número final de lâmpadas guardado na variável unidades.

#print(f"Total de lâmpadas que devem ser instaladas: {unidades}")


