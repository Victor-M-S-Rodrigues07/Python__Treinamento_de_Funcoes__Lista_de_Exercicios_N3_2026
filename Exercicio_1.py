ano_nascimento = int (input ("Digite o ano de nascimento do aluno: "))
ano_atual = 2026

def calcular_idade (ano_nascimento, ano_atual = 2026):

    idade = ano_atual - ano_nascimento

    return idade

print (f"O(a) aluno(a) tem:  {calcular_idade (ano_nascimento, ano_atual)} anos de idade")