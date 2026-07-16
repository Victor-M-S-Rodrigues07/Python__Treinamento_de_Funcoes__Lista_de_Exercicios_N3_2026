def conversor_int (lista_usuario):

    """ Converte uma lista de strings para lista de inteiros"""

    return [float (valor) for valor in lista_usuario]

def soma_lista (lista_usuario):

    soma = 0

    for numero in lista_usuario:

        soma += numero
    
    return soma

lista_linha_usuario = input ("Digite os valores em linha, sem 'R$', separados por espaços: ").split()
lista_convertida = conversor_int (lista_linha_usuario)

print (f"\nResposta: R${soma_lista (lista_convertida)}")