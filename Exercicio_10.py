def soma_recursiva (contador, numero_limite):

    if contador == numero_limite:

        return numero_limite
    
    return contador + soma_recursiva (contador + 1, numero_limite)

limite_usuario = int (input ("Digite um número para ser o limite da soma: "))
numero_inicio = int (input ("Digite um número para ser o início da soma: "))

print ("O resultado é ", soma_recursiva (numero_inicio, limite_usuario))