"""
Métodos representam os comportamentos do objeto.
Ou seja, as ações que o objeto pode representar no sistema

Os métodos são divididos em métodos de instância
e métodos de classe
métodos mágicos = dunder = __init__ etc

"""


# métodos de instancia (precisa de estar instanciado para usá-lo)
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

    def __acender__(self, quantidade):  # não é recomendável criar métodos assim
        print(f"{self.__cor} em {quantidade} de luminosidade")

    def apagar(self):
        print("Lampada apagada")


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo


lampada = Lampada('red', 12, 2)
lampada.__acender__(3)  # faz instancia para pegar o método.
print(lampada._Lampada__cor)  # acesso incorreto ao atributo de classe,pois ele é privado (manglin)
Lampada.apagar(lampada)  # assim tambem funciona, pois a lampada recebe o objeto


#  métodos de classe, usa-se um decorator, para indicar (é mais correto)
class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    @classmethod  # conhecido como método static em outras linguagens
    def imprimeNome(cls):  # não recebe self como parâmetro
        print("NOME")


Usuario.imprimeNome()
user = Usuario('ok', 123)
user.imprimeNome()

"""
Quando usar? 
Quando precisar fazer acesso a atributos, cria-se metodos de instancia
quando não, métodos de classe
"""


# métodos privados
class Teste:
    contador = 0

    @classmethod
    def __geraUser(cls): # npetidi oruvadi
        print("HELLO")

    @classmethod
    def usaMetododeClasse(self):
        print(self.__geraUser())

Teste.usaMetododeClasse()


# método estático
class OK:
    @staticmethod
    def estatico():
        return "OK, GOOGLE!"

lulaPuto = OK.estatico()
print(lulaPuto)
print(OK.estatico())


