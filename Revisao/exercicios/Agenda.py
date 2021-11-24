# armazenar, remover, buscar, imprimir
class Agenda:
    indice = 0  # atributo de classe (static)
    agenda = []

    def __init__(self, nome, idade, altura):
        """
        método construtor para criar objetos
        :param nome:
        :param idade:
        :param altura:
        """
        # atributos de instância:
        self.nome = nome
        self.__idade = idade
        self.__altura = altura
        self.contador = Agenda.indice + 1
        Agenda.indice += 1 # atualiza o valor do índice

    def insere(self):
        """
        insere a pessoa e retorna a lista
        :return:
        """
        dicionario = dict()
        dicionario['nº'] = self.contador
        dicionario['nome'] = self.nome
        dicionario['idade'] = self.__idade
        dicionario['altura'] = self.__altura
        if dicionario['nº'] in Agenda.agenda:
            pass
        else:
            Agenda.agenda.append(dicionario)
        return Agenda.agenda

    def remove(self, nomeAremover):
        """
        Remove a pessoa passada
        :param nomeAremover:
        :return:
        """
        remover = False
        posicao = 0
        p = 0
        for i in range(len(Agenda.agenda)):
            remover = nomeAremover in Agenda.agenda[i].values()
            if remover:
                p = i
                posicao = Agenda.agenda[i]['nº']
                break
        if remover:
            if Agenda.agenda[p]['nº'] == posicao:
                del Agenda.agenda[p]
            return "Removido(a)"
        else:
            return "Não encontrado"

    def exibir(self):
        """
        procedimento que exibe, apenas
        :return:
        """
        for itens in Agenda.agenda:
            print(itens)

    def presente(self, nome):
        """
        verifica se está presente na lista, retorna texto com a posição
        :return:
        """
        for pessoas in Agenda.agenda:
            if nome in pessoas.values():
                return f"numero da pessoa informada: {pessoas['nº']}"

if __name__ == '__main__':
    lista = [["Mateus", 23, 1.75], ["Ms", 24, 2.75]]
    # cabeçalho
    agenda = Agenda("NOME".center(5), "IDADE".center(5), "ALTURA".center(5))
    for pessoas in lista:
        agenda.__init__(pessoas[0], pessoas[1], pessoas[2])
        agenda.insere()
    agenda.exibir()
    print(agenda.presente("Ms"))
    # agenda.remove('Mateus')
    # agenda.exibir()
