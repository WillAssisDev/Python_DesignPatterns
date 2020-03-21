from abc import abstractmethod


class Estado:

    @abstractmethod
    def avanca(self, fabrica):
        pass

    @abstractmethod
    def recua(self, fabrica):
        pass


class EstadoInicial(Estado):

    def __str__(self):
        return 'Estado Inicial'

    def avanca(self, fabrica):
        fabrica.muda_estado(EstadoFinal())

    def recua(self, fabrica):
        raise Exception('#ERRO: Está no estado inicial.')


class EstadoFinal(Estado):

    def __str__(self):
        return 'Estado Final'

    def avanca(self, fabrica):
        raise Exception('#ERRO: Está no estado final.')

    def recua(self, fabrica):
        fabrica.muda_estado(EstadoInicial())


class Fabrica:

    def __init__(self):
        self.__estado = EstadoInicial()

    @property
    def estado(self):
        return self.__estado

    def muda_estado(self, novo_estado):
        self.__estado = novo_estado

    def avanca(self):
        self.__estado.avanca(self)

    def recua(self):
        self.__estado.recua(self)


if __name__ == '__main__':
    fabrica = Fabrica()
    print(fabrica.estado)
    fabrica.avanca()
    print(fabrica.estado)
    fabrica.recua()
    print(fabrica.estado)
    fabrica.recua()