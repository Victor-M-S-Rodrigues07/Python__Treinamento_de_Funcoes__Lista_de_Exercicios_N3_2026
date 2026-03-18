def verificador_de_paridade (numero):

    return numero % 2 == 0

lista_numeros_usuario = input ("Digite uma sequência de números, separando por espaços: ").split()
lista_convertida = list (map (int, lista_numeros_usuario))

# Função Build-In Map() => Aplica a função a todos os elementos de um iterável, como listas ou tuplas

# Função Build-In Filter()

endereco_dos_numeros_filtrados = filter (verificador_de_paridade, lista_convertida)
lista_filtrada = list (endereco_dos_numeros_filtrados) # Se não retorna "Números pares: <filter object at 0x0000024BA6834550>"

# Nota: ele vai retornar o endereço da memória da lista, não a lista em si. Tu precisa colocar em uma variavel
print (f"\nNúmeros pares: {lista_filtrada}")