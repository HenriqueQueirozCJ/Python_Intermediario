#*args -> Argumentos não nomeados

x,y,*resto = 1,2,3,4
print(x,y,resto)

def soma(*args):
    total=0
    for numero in args:
        total += numero
    return total

soma(1,2,3,4,5,1,2,3)
# print(soma(1,2,3))

#args2

num=(1,2,3,4,5,6,7)
soma3 = soma(*num)
print(soma3)
# print(sum())
print(*num)


