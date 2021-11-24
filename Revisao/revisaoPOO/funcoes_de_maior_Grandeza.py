# funções de maior grandeza-higher order functions (hof)

# ou seja, uma funcao retorna outra funcao ou recebe uma funcao
"""
em python, funcoes sao consideradas primeira classe
"""
# exemplo:


def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def calcular(a, b, funcao):
    return funcao(a, b) # aqui tem-se um HOF, pois uma funcao retorna outra;


print(calcular(1, 2, soma)) # soma nao pode ser passada aberta, pois se nao , executará no parâmetro e so entrara o retorno
print(calcular(1, 2, diminuir))



# nested functions - funções aninhadas:
# pode-se, em python, ter funções dentro de funções
# são funções internas


from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('ola', 'sai fora'))
    return humor() + ', '+ pessoa


print(cumprimento('Nome'))


def faz_me_rir():
    def rir():
        return choice(('hahaha', 'kkkkkk'))
    return rir # retorna a funcao sem executar. So executa quando quer


rindo = faz_me_rir()
print(rindo())