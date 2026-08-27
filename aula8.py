def calculadora_v1():  

    num1 = float(input("Digite seu primeiro número: "))
    num2 = float(input("Digite seu segundo número: "))
    operador = input("Informe a operação desejada entre: 1. adição; 2. subtração; 3. multiplicação e 4. divisão: ")


    match operador:
        case "1":
            print(f"Resultado da soma: {num1 + num2}.")
        case "2":
            print(f"Resultado da subtração: {num1 - num2}.")
        case "3":
            print(f"Resultado da multiplicação: {num1 * num2}.")
        case "4":
            
            if num2 != 0:
                print(f"Resultado da divisão: {num1 / num2}.")
            else:
                print("Dividiu por zero, errou feio!")
        case _:
            print("Informe um operador válido.")


calculadora_v1()




    





       
    










