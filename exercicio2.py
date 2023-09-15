# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multi(multip):
    def multipl(numero):
        return numero * multip
    return multipl
    
duplicar = multi(2)
triplicar = multi(3)
quadruplicar = multi(2)

print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))