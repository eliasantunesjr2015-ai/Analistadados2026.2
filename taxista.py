# dados usados para saber o lucro do taxista

# Valor fixo do preço do combustível
PRECO_COMBUSTIVEL = 6.15

# Coleta dos dados do dia de trabalho
km_inicial = float(input("Digite a quilometragem no INÍCIO do dia: "))
km_final = float(input("Digite a quilometragem no FINAL do dia: "))
litros_gastos = float(input("Digite a quantidade de litros consumidos (L): "))
faturamento_total = float(input("Digite o valor total recebido dos passageiros (R$): "))

# Processamento e cálculos do rendimento
distancia_percorrida = km_final - km_inicial
media_consumo = distancia_percorrida / litros_gastos
gasto_combustivel = litros_gastos * PRECO_COMBUSTIVEL
lucro_liquido = faturamento_total - gasto_combustivel

print("\n--- RESUMO DO DIA ---")
print(f"Distância total percorrida: {distancia_percorrida:.1f} km")
print(f"Média de consumo do veículo: {media_consumo:.2f} km/L")
print(f"Gasto com combustível: R$ {gasto_combustivel:.2f}")

# Avaliação do resultado financeiro usando a estrutura if/elif/else
if lucro_liquido > 0:
    resultado_financeiro = f"Lucro Líquido de R$ {lucro_liquido:.2f}"
elif lucro_liquido < 0:
    resultado_financeiro = f"Prejuízo de R$ {abs(lucro_liquido):.2f}"
else:
    resultado_financeiro = "Empate (o faturamento cobriu apenas os custos)"

print(f"Resultado final do dia: {resultado_financeiro}")





#O programa lê os quilômetros (inicial e final), os litros de combustível usados e o dinheiro ganho dos passageiros via input().

#calcula a quilometragem rodada e divide pelos litros para achar a média de consumo (media_consumo). Depois, multiplica os litros pelo preço fixo de R$ 6,15 e subtrai do faturamento para achar o lucro líquido.

#distancia_percorrida = km_final - km_inicial

#(if/elif/else): Ele avalia o saldo financeiro: se for maior que zero, define como Lucro; se for menor, define como Prejuízo; se for igual, define como Empate.

 #Exibe no terminal a média de km/L do carro e o resultado financeiro do dia do motorista.
#print(f"Resultado final do dia: {resultado_financeiro}")










