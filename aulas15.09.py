##Escopo de Funções##

x=10
def escopo():
    x=11
    def escopo2():
        x=12
        print(x)
    print(x)
    escopo2()
    
print(x)
escopo()
print(f'O resultado do {x=} global e + 3 e igual a {x+3=}')
print(2**2)

#retorno do valores das funções
