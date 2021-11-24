"""
Decorators -> são funções que envolvem outras funções e aprimoram seus comportamentos
eles são Higher order functions e usa-se @(syntact sugar)

"""

# syntax não recomendada:


def seja_educado(funcao):
    def sendo():
        print("OK")
        funcao()
        print("bom dia")
    return sendo


def saudacao():
    print("Seja bem vindo(a)")


teste = seja_educado(saudacao)
teste() # ou seja, o decorator colocou mais atributos na função


# sintaxe recomendada:
def seja_muito_educado(funcao):
    def sendo_mesmo():
        print("Olá")
        funcao()
        print("Muito obrigado")
    return sendo_mesmo

@seja_muito_educado
def agradecer():
    print("Vou agradecer")


agradecer()


### receber mais de 1 parametro

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome, google): # dois parametros geraria error, para isso, usa-se Decorator pattern (args e kwargs)
    return f'Olá, {nome}, {google}'
@gritar
def ola(d,**mane):
    return f'opa {mane}'


print(saudacao('ok', 'mané'))
print(ola(1, o='kd'))

"""
decorators com argumentos de entrada
"""

def verifica(valor):
    def ok(s):
        def o(*args):
            print(args)
            if args == valor:
                return 'Valor correto'
            else:
                return 'valor incorreto'
        return o
    return ok

@verifica('1')
def sok():
    print("1")
    return ()
print(sok())