def contador_caracteres (palavra, limite):

    quantidade_letras = len (palavra)

    print (f"A palavra {palavra} contém {quantidade_letras} caracteres")

    if quantidade_letras > limite:

        print ("\nAtenção, limite máximo de caracteres atingido!\n")

palavra_usuario = input ("Digite uma palavra: ")
limite_usuario = int (input ("Qual é o limite de caracteres da avaliação? R: "))
contador_caracteres(palavra_usuario, limite_usuario)