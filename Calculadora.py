
def calculadora():
   
    #menu de opções
    while True:
        print("***********Menu de opções************")
        print("+ : Adição")
        print("- : Subtração")
        print("* : Multiplicção")
        print("/ : Divisão")
        print("Saída = s ")
        print("hist")
        Operador=input("Escolha uma opção")


        #lista de operadores válidos
        operadores_validos=["+","-","*","/","s","hist"]

        #Erros/Opção inválida
        if Operador not in operadores_validos:
            print("ERRO! Escolha apenas as opções disponíveis.")
            continue  # volta ao início do loop

         #Sair do loop
        elif Operador == "s":
            break

        # Exibir histórico
        elif Operador == "hist":
            if lista_contas:
                print("Histórico de operações:\n")
                print(lista_contas)
            else:
                print("Ainda não foram realizadas operações.")
            continue  # Volta ao menu

 
   # função principal

        #Entrada de números
        num1=float(input("Insira o primeiro numero: "))
        num2=float(input("Insira o segundo numero: "))

         #Operações
        if Operador == "+" :
            result = num1 + num2
            print(" O resultado é: " + str(result))
            lista_contas.append( str(num1) + " + " + str(num2) + " = " + str(result))

        elif Operador == "-" :
            result = num1-num2
            print(" O resultado é: " + str(result))
            lista_contas.append(str(num1) + " - " + str(num2) + " = " + str(result))

        elif Operador == "/":
            result = num1/num2
            print(" O resultado é: " + str(result))
            lista_contas.append( str(num1) + " / " + str(num2) + " = " + str(result))

        elif Operador == "*":
            result = num1*num2
            print(" O resultado é: " + str(result))
            lista_contas.append( str(num1) + " * " + str(num2) + " = " + str(result))




calculadora()

 
