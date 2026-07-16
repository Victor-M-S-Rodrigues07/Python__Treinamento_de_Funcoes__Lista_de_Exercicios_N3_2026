def concatenador_de_listas (lista_produtos, lista_precos):

    lista_final = []
    i = 0

    for produto in lista_produtos:

        lista_final.append ({"produto": produto, "preco": float(lista_precos[i])})
        i += 1
        
    return lista_final
    
def exibir_lista (lista_final):

    for item in lista_final: 
        print (f"{item["produto"]} = R${item["preco"]}\n")



lista_produtos = input ("Digite os produtos da lista, separados por vírgula (,): ").split (", ")
lista_precos = input ("Digite os preços de cada produto da lista, seguindo o mesmo modelo anterios -- separando por vírgulas: ").split (", ")

try:
    lista_precos_convertida = list (map (float, lista_precos))
    lista_final = concatenador_de_listas (lista_produtos, lista_precos_convertida)
    exibir_lista (lista_final)

except ValueError:

    print ("Ocorreu um erro. Digite somente números no campo de preços.")