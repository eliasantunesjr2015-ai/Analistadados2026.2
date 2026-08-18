
# Ordenação de três números


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


# Estrutura condicional para ordenar os números

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        meio = num1
        maior = num2
    else:
        meio = num2
        maior = num1

# Mostre o resultado ordenado

print(f"Números ordenados: {menor}, {meio}, {maior}")















