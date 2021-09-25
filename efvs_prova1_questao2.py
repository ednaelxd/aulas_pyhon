#Questão 2
cont_p=0
coeficientes=[]
x=calculo=float()
n_para=True

while n_para:
    grau_polinomio=int(input('Digite o grau do polinômio: '))
    while cont_p <= (grau_polinomio):
        coeficientes.append(float(input(f'Digite o {cont_p}-esimo coeficiente: ')))
        cont_p += 1
    x=float(input('Digite um valor x para ser testado: '))
    for i in range(0,grau_polinomio+1):
        calculo+=coeficientes[i]*(x**(i))
    print("O valor da função é:",calculo)
    cont_p=0
    if (calculo==0):
        n_para=False
    calculo=0
    coeficientes=[]
