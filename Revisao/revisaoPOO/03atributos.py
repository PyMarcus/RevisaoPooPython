"""
atributos são as características do objeto.Ou seja, são os estados de um
objeto

atributos de instancia => atributos declarados dentro do método construtor, ou seja, todos objetos terão esses atributos
atributos de classe => atributos declarados diretamente na classe , fora do construtor.Geralmente, esses atributos já têm um tipo inalterável
atributos dinâmico =>

"""


# obs o parâmetro self chama-se self por convenção, poderia ser qualquer nome

class Lampada:
    def __init__(self, voltagem, cor):  # método construtor (cria objetos)
        """
        atributos de instancia
        :param voltagem:
        :param cor:
        """
        # private = .__ (acessado só dentro da classe)
        self.__voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):  # self é o objeto que está executando o método
        """
        atributos de instancia
        :param numero:
        :param limite:
        :param saldo:
        """
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


"""
Atributos públicos e privados
privados=>acesso dentro da própria classe
público=>acesso fora da classe
"""


# por convenção, todo atributo de uma classe é públic
class Atributos:
    def __init__(self, atributoPrivado, atributoPublico):
        self.__atributoPrivado = atributoPrivado  # name mangling
        self.atributoPublico = atributoPublico


lamp = Atributos(10, 2)
print(dir(lamp))
print(lamp._Atributos__atributoPrivado)  # temos acesso,mas não deveríamos ter, isso é o name mangling

"""
atributos de classe:
"""


class Produto:
    # atributo de classe
    imposto = 1.05 # 0.05%

    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor * Produto.imposto


produto = Produto("ps4", 2939)
print(round(produto.valor))
print(produto.imposto)

# nao se precisa criar uma instancia para fazer acesso a um atributo de classe
# em java, os atributos de classe são chamados atributos estáticos
# atributos de classe utilizam menos memória

"""
atributos dinâmicos
"""
# são atributos de instancia criados em tempo de execução e será exclusivo da instancia

p1 = Produto("ps5", 2030)
p1.peso = '1kg' # cria o atributo dinâmico
print(p1.__dict__)

# deletar atributos dinamicamente:
del p1.peso

print(p1.__dict__)  # exibe as propriedades do objeto