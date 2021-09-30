def menu():
    print("__________________________________________")
    print("| Bem vindo ao nosso sistema de registro |")
    print("|     O que você deseja fazer hoje?      |")
    print("||||||||||||||||||||||||||||||||||||||||||")
    print("|1.||Ver|as|informações|dos|jogadores|||||")
    print("|2.|Inserir|dados|de|um|novo|player|||||||")
    print("|3.||Atualizar|informações|de|um|player|||")
    print("|4.||Apagar|uma|conta|existente|||||||||||")
    print("|5.||Consultar|dados|de|um|jogador||||||||")
    print("|6.||||||||||||||E|X|I|T||||||||||||||||||\n")

def le_banco(nome_do_arquivo,dic_local):
    arq = open(nome_do_arquivo,"r")#abertura do arquivo
    linhas_arq = arq.readlines()
    lista_logins=[]
    infos_personagens=[]
    cabecalhos_dados=[]
    dic_geral={}
    i=0 #contador das linhas
    n=0 #contador dos personagens
    j=0 #contador de apoio
    while i<len(linhas_arq):
        #salvar logins como chaves do dicionario externo
        #salvar nomes dos atributos como chaves e os pontos e nomes como valores
        if ((i-n*14)==0): #captura de logins
            lista_logins.append(linhas_arq[i][linhas_arq[i].index(": ")+2 : linhas_arq[i].index("\n")])
        elif((i-14*n)==3):#captura as classes dos personagens
            infos_personagens.append(linhas_arq[i][linhas_arq[i].index(": ")+2:linhas_arq[i].index("\n")])
            cabecalhos_dados.append(linhas_arq[i][:linhas_arq[i].index(": ")])
            j+=1
        elif (i-14*n)>=7 and (i-14*n)<=12: #captura os atributos dos personagems
            #Fiz dessa forma pra depois não ter que percorrer os dados novamente, soh pra converter em numero
            infos_personagens.append(int(linhas_arq[i][linhas_arq[i].index(": ")+1:linhas_arq[i].index("\n")]))#valor atb
            cabecalhos_dados.append(linhas_arq[i][:linhas_arq[i].index(": ")])#atrib
            j+=1
            #print(dic_atb)
            if(j%7==0 and j>0):
                dic_geral[lista_logins[n]]=dict(zip(cabecalhos_dados[:j],infos_personagens[:j]))
                cabecalhos_dados=[]
                infos_personagens=[]
        if ("***" in linhas_arq[i]): #captura o fim de dados de um personagem
            n+=1
        i+=1
    dic_local=dic_geral.copy()
    arq.close()#fechamento do arquivo
    return(dic_local)

def busca_jogador(dic_local,jogador):
    if(jogador in dic_local):
        print("O jogador possui conta registrada!")
        resp=input("Deseja ver os dados do jogador em questao? (Y/N)")
        if resp=="Y":
            print("")#imprime_dados...
        elif resp=="N":
            print("Redirecionando para menu\n")
        else:
            return ValueError
    else:
        print("Jogador nao encontrado!")
        resp2=input("Deseja cadastra-lo? (Y/N)")    
        if(resp2=="Y"):
            print("")#cadastra_jogador...
        elif resp2=="N":
            print("Redirecionando para menu\n")
        else:
            return ValueError

def imprime_dados(dic_local):
    for nick,atrib in dic_local.items():
        print("||||||||||||||")
        print(nick)
        print("||||||||||||||")
        for dados in atrib:
            print(dados,":",atrib[dados])

def adiciona_itens(arquivo_name,dic_local):
    arq=open(arquivo_name,"w")
    invalido=True
    while invalido:
        nome_nv=input("Digite o nome do novo jogador")
        if(nome_nv in dic_local.keys()):
            invalido=True
            print("Nick jah existente")
        else:
            invalido=False
            #############
    classe_nv=input("Qual a classe do novo player (Mago/Guerreiro)")
    forca_nv=int(input("Quantos pontos tera de forca? "))
    agi_nv=int(input("Quantos pontos tera de agilidade? "))
    vit_nv=int(input("Quantos pontos tera de vitalidade? "))
    inteligencia_nv=int(input("Quantos pontos tera de inteligencia? "))
    des_nv=int(input("Quantos pontos tera de destreza? "))
    luk_nv=int(input("Quantos pontos tera de sorte? "))
    ##########
    dic_local[nome_nv]={"Classe do personagem":classe_nv,
                     "Forca":forca_nv,
                     "Agilidade":agi_nv,
                     "Vitalidade":vit_nv,
                     "Inteligencia":inteligencia_nv,
                     "Destreza":des_nv,
                     "Sorte":luk_nv}
    i=0
    for nick,atrib in dic_local.items():
        if(i==0):
            arq.write("login: "+nick+"\n")
            arq.write("senha: 123123\n\n")
        if(i>0): #condicao pra garantir o padrao da linha 0
            arq.write("\nlogin: "+nick+"\n")
            arq.write("senha: 123123\n\n")

        for dados in atrib:
            arq.write(dados+": "+str(atrib[dados])+"\n")
            #print(atrib["Classe do personagem"],i)
            if(atrib["Classe do personagem"]=="Mago" and i%7==0):
                arq.writelines("\nAtributos:\n\n")
            if(atrib["Classe do personagem"]=="Guerreiro" and i%7==0):
                arq.writelines("\nAtributos:\n\n")
            i+=1
            #print(i)
        arq.writelines("**********************************")
    arq.close

def atualiza_itens(dic_local,nome_arquivo):
    i=0
    arq=open(nome_arquivo,"w")
    print("Para essa funcao precisamos saber o voce deseja modificar")
    print("Opcoes disponiveis:\nClasse do char\nValores dos atributos")
    nick=input("Insira seu nick: ")
    if nick in dic_local:
        dic_local[nick]["Classe do personagem"]=input("Qual nova classe voce deseja ser?(Mago/Guerreiro) ")
        print("Agora vamos redistribuir seus pontos de habilidade")
        #futuramente incorporar uma contagem de pontos disponiveis, para limitar a operacao
        dic_local[nick]["Forca"]=int(input("Quantos pontos tera de forca? "))
        dic_local[nick]["Agilidade"]=int(input("Quantos pontos tera de agilidade? "))
        dic_local[nick]["Vitalidade"]=int(input("Quantos pontos tera de vitalidade? "))
        dic_local[nick]["Inteligencia"]=int(input("Quantos pontos tera de inteligencia? "))
        dic_local[nick]["Destreza"]=int(input("Quantos pontos tera de destreza? "))
        dic_local[nick]["Sorte"]=int(input("Quantos pontos tera de sorte? "))
    if nick not in dic_local:
        print("Usuario inexistente")
    for nick,atrib in dic_local.items():
        if(i==0):
            arq.write("login: "+nick+"\n")
            arq.write("senha: 123123\n\n")
        if(i>0): #condicao pra garantir o padrao da linha 0
            arq.write("\nlogin: "+nick+"\n")
            arq.write("senha: 123123\n\n")

        for dados in atrib:
            arq.write(dados+": "+str(atrib[dados])+"\n")
            #print(atrib["Classe do personagem"],i)
            if(atrib["Classe do personagem"]=="Mago" and i%7==0):
                arq.writelines("\nAtributos:\n\n")
            if(atrib["Classe do personagem"]=="Guerreiro" and i%7==0):
                arq.writelines("\nAtributos:\n\n")
            i+=1
        arq.writelines("**********************************")
    arq.close()

def remove_itens(dic_local,arquivo):
    i=0
    arq=open(arquivo,"w")
    deletado=input("Digite o login da conta que deseja deletar: ")
    del dic_local[deletado]
    for nick,atrib in dic_local.items():
        if(i==0):
            arq.write("login: "+nick+"\n")
            arq.write("senha: 123123\n\n")
        if(i>0): #condicao pra garantir o padrao da linha 0
            arq.write("\nlogin: "+nick+"\n")
            arq.write("senha: 123123\n\n")

        for dados in atrib:
            arq.write(dados+": "+str(atrib[dados])+"\n")
            #print(atrib["Classe do personagem"],i)
            if(atrib["Classe do personagem"]=="Mago" and i%7==0):
                arq.writelines("\nAtributos:\n\n")
            if(atrib["Classe do personagem"]=="Guerreiro" and i%7==0):
                arq.writelines("\nAtributos:\n\n")
            i+=1
        arq.writelines("**********************************")
    arq.close()

#funcionalidade das senhas, sera adicionada em versoes futuras
def dados_jogo():
    #inicializacao\\\
    continua=True
    dic_local={}
    dic_local=le_banco(input("Digite o nome do arquivo: "),dic_local)#Leitura do arquivo
    #///
    #print(dic_local)
    while continua:
        menu()
        #print(dic_local)
        users_choice=int(input("Digite o número correspondente daquilo que voce deseja, aventureiro!  "))
        #Impressao dos dados
        if(users_choice==1):
            imprime_dados(dic_local)
        #Particao para adição de itens
        if(users_choice==2):
            adiciona_itens(input("Digite o nome do arquivo txt"),dic_local)
        #Particao para atualizacao
        if(users_choice==3):
            atualiza_itens(dic_local,input("Insira o nome do arquivo: "))
        #Particao para remoção de itens
        if(users_choice==4):
            remove_itens(dic_local,input("Insira o nome do arquivo: "))
        #Particao de busca
        if(users_choice==5):
            busca_jogador(dic_local,input("Por qual jogador voce busca? "))
        if(users_choice==6):
            continua=False
dados_jogo()