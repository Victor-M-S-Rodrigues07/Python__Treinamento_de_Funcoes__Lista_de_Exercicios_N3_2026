try:

    numero_usuario_1 = int (input ("Digite um número: "))
    numero_usuario_2 = int (input ("Digite outro numero: "))
    operacao_usuario = input ("Escolha o operador a ser utilizado (+, -, * ou /): ")

    if operacao_usuario == "+":

        soma = lambda N1, N2: N1 + N2;

        print (f"Resultado = {soma (numero_usuario_1, numero_usuario_2)}")

    elif operacao_usuario == "-":

        subtracao = lambda N1, N2: N1 - N2;

        print (f"Resultado = {subtracao (numero_usuario_1, numero_usuario_2)}")
    
    elif operacao_usuario == "*":

        multiplicacao = lambda N1, N2: N1 * N2;

        print (f"Resultado = {multiplicacao (numero_usuario_1, numero_usuario_2)}")

    elif operacao_usuario == "/":

        divisao = lambda N1, N2: N1 / N2;

        print (f"Resultado = {divisao (numero_usuario_1, numero_usuario_2)}")
    
    else:

        print ("Digite uma operação válida!")

except ValueError: 
    
    print ("Digite um número válido")