def personalizar_saudacao (horario):

    if horario < 12:

        print ("Bom dia!")
    
    elif 12 <= horario <= 18:

        print ("Boa tarde!")
    
    elif 18 < horario <= 23:

        print ("Boa noite!")

    else:

        print ("Digite um horário válido!!")

horario_atual = int (input ("Digite o horário atual (0 - 23): "))
personalizar_saudacao (horario_atual)