"""
POO visa encapsular o código em um grupo lógico e hierárquico usando
classes

Ou seja, classes encapsulam métodos e atributos

Abstração -> exibe apenas dados relevantes de uma classe e escondendo métodos e atributos do user
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def __metodo(self):  # método privado
        print("ok")


pessoa = Pessoa('José', 23)
try:
    pessoa.__metodo()  # tentativa de acesso ao método privado( acesso apenas na classe)
except AttributeError:
    print("ERRO IGNORADO")
    pass
finally:
    pessoa._Pessoa__metodo()  # manglin (incorreto) para acessar


# obs: o problema em se definir como público está em poder acessar e alterar os atributos da classe
# ou seja, utilizar atributos e métodos privados fazem com que a classe encapsule de fato os atributos e métodos


class Banco:
    def __init__(self, nome, valor, saldo):
        self.__nome = nome
        self.__valor = valor
        self.__saldo = saldo

    def extrato(self):
        print(self.__saldo ,'reais')

    def transferencia(self, valor, contadestino):
        contadestino.__saldo += valor # insere valor no objeto, alterando seu atributo e por estar dentro da classe, funfa
        self.__saldo -= valor  # retira o valor depositado de self, ou seja, do objeto
        return "transferido"


conta1 = Banco('j', 1000, 2000)
conta2 = Banco('r', 1222, 1039)
conta1.extrato()
conta2.extrato()
conta1.transferencia(22, conta2)
conta1.extrato()
conta2.extrato()