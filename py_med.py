#Definindo Funções que podem ser repetidas no código#

def kappa(a,b,c):
    print(a,b,c)

kappa(1,2,3) 
kappa(4,5,6)   

def ola(nome):
    print(f"Olá {nome}!")

ola("Henrique")
ola("Maria")
ola("Gabriel")

#Argumentos = valor Nomeados e não nomeados#
#Argumentos posicionais dependem da ordem#

def soma (x , y, z): #parametros
    print(x + y + z )
    print(f"{x=},{y=},{z=} | x + y + z = ", x+y+z)
soma(1,2,5)
