"""
Objetos são instâncias de classe.Ou seja, é a materialização de uma
classe no mundo computacional.Eles,portanto, têm um endereço de memória.

"""


class Lampada:

    redutor = 0

    def __init__(self, cor, voltagem, luminosidade):  # método construtor cria um objeto e o inicializa
        self.__cor = cor # self é como se fosse o título, mas, fazendo referência ao próprio objeto this no Java
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False

    @classmethod
    def reduz(cls):
        Lampada.redutor = 1
        return Lampada.redutor

    def liga_lampada(self):
        self.ligada = True
        return self.ligada

    def apaga_lampada(self):
        if self.ligada:
            self.ligada = False
        return self.ligada

    def reduz_luminosidade(self):
        self.__luminosidade -= Lampada.reduz()
        return self.__luminosidade

    def printa(self):
        print(self.__luminosidade)

# criando o objeto


lampada = Lampada('branca', 110, 60)
print(lampada.liga_lampada()) # liga a lampada, muda para true
print(dir(lampada))
print(lampada.ligada)
print(lampada.apaga_lampada())
print(lampada.ligada)
print(lampada._Lampada__luminosidade) # manglin (incorreto)
print(lampada.printa())
print(lampada.reduz_luminosidade())
print(lampada.reduz_luminosidade())
print(lampada.reduz_luminosidade())
print(lampada.reduz_luminosidade())
print(lampada.reduz_luminosidade())
print(lampada.printa())