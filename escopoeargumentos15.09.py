#Escopo de Funções

x=1
def kappa():
    x=3
    def kappa2():
        x=10
        print(x)
    kappa2()    
    print(x)
print(x)
kappa()

#Argumentos

def soma(x=3,y=2,z=None):
    print(f'{x=}|{y=}|{z=} | {x+y=}!')
    ...
soma()