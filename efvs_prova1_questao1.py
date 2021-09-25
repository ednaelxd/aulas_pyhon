#Questão 1

cadastro_pessoas=[]
contador=conta_mulheres=mais_velho=rendas_todas=0
parada_geral=True
nome=str()
idade=int()
renda=float()
parada_sexo=False
while parada_geral:
    #Início do código - SEXOS
    while not parada_sexo:
        sexo=input(f'Digite o SEXO do {contador+1}º cidadão: ')
        if (sexo=="M" or sexo=="F"):
            parada_sexo=True
        if (sexo=="F"):
            conta_mulheres+=1
    #Fim - SEXOS
    #######################################F
    #Início do código - IDADES E RENDA
    idade= int(input(f'Digite a IDADE do {contador+1}º cidadão: '))

    if(idade<0):
        parada_geral=False
    elif(idade>0): # Só vai ser inserida a renda, caso não haja pedido de parada (numero negativo)
        renda=float(input(f'Digite a RENDA do {contador+1}º cidadão: '))
        if(mais_velho<idade):
            mais_velho=idade
        rendas_todas+=renda
        contador+=1
        parada_sexo=False
    #Fim - IDADES E RENDA

renda_media=rendas_todas/contador
proporcao_mulheres=(conta_mulheres/contador)*100
print("O total de pessoas cadastradas foi de",contador)
print(f"A proporção de mulheres é de {proporcao_mulheres}%")
print("A pessoa com maior idade possui",mais_velho,"anos")  
print(f"A média das rendas é de ${renda_media}")