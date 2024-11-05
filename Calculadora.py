
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
