 # Cálculo dé Média e Status do Estudante


# Digite as notas do estudante:

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))


# Calcula as Médias do estudante
media = (nota1 + nota2 + nota3 + nota4) / 4


# Exibe a média calculada com duas casas decimais
print(f"Média final: {media:.2f}")

# Verifique o status do estudante com as condicionais
if media > 7:
    print("Status: Aprovado")
elif 5 <= media <= 7:
    print("Status: Recuperação")
else:
    print("Status: Reprovação")
















