"""
POO é a programação orientada à objetos que mapeia objetos do mundo real para
modelos computacionais

Elementos principais:
classe => modelo do objeto do mundo real representado computacionalmente
atributo => característica do objeto
método => comportamento do objeto
construtor => método especial que cria objetos
objeto => instancia de dados


obs: com POO, cria-se o próprio tipo abstrato de dados
"""
from os.path import realpath

print(realpath(__file__))

class Produto:
    pass


ps4 = Produto()  # construtor da classe produto instancia um objeto chamado ps4
