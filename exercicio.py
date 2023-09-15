# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def argmult(*args):
    total = 1
    for numargs in args:
        total *= numargs
    return total
multi = argmult(1,2,3,4,5)
print(multi)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def parimpar(numero):
    multi = numero % 2 == 0
    if multi:
        return(f"{numero} e par")
    return(f"{numero} e impar")

par_impar = parimpar
dois_par = par_impar(3)
print(dois_par)
print(parimpar is parimpar)
