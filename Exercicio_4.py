def conversor_inteiro (lista_de_numeros):

    lista_atualizada = []

    for numero_lista in lista_de_numeros:

        try:

            numero_lista = int (numero_lista)
            # print (numero_lista)
            # print (isinstance (numero_lista, int)) Testes

            lista_atualizada.append (numero_lista)
        
        except ValueError:

            return "Há elementos que não são strings na lista enviada\n"

    return lista_atualizada

def checagem_de_conversoes (lista_de_numeros):

    for numero_lista in lista_de_numeros:
        
        if not isinstance (numero_lista, int):

            return "Houve um erro na conversão, tente novamente\n"
        
    return "Todos os números foram convertidos!"

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

lista_verificada = conversor_inteiro (telefones)
print (lista_verificada)
print (checagem_de_conversoes (lista_verificada))