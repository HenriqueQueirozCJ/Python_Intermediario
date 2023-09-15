#retorno das funções#

kappa = print("Henrique\n")
print(kappa) #Valor padrão das funções é None Type

def soma(x,y):
    return (x+y) #com a função return será possível usar a função para execução correta#
                 #return só executará funções que a antecedem, pois possui um valor que determina
                 #o fim da função, cada função poderá carregar um return

soma1 = soma(2,3)
soma2 = soma(2,3)
print(soma1 + soma2)