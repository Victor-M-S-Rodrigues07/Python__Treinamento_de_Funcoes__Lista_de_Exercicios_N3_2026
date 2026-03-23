def closure_calculador_de_desconto (procentagem_desconto):

    def aplicar_desconto (preco):

        return preco - (preco * procentagem_desconto / 100)
    
    return aplicar_desconto

desconto = int (input ("Digite a porcentagem do desconto a ser aplicado (em %): "))
funcao_desconto = closure_calculador_de_desconto (desconto) # A variável armazena a função de dentro

preco_produto = float (input ("Digite o preço do produto (sem o R$): "))
print (f"O preço final com desconto é: R${funcao_desconto (preco_produto):.2f}") # Display semelhante ao %f.2 do C