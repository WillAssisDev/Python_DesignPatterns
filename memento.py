class Estado:

    def __init__(self, estado):
        self.__estado = estado

    def __repr__(self):
        return self.__estado.nome

    @property
    def estado(self):
        return self.__estado


class Historico:

    def __init__(self):
        self.__estados = []

    def __call__(self, indice):
        return self.__estados[indice]

    def __iadd__(self, estado):
        self.__estados.append(estado)
        return self

    def adiciona(self, estado):
        self.__estados.append(estado)

    @property
    def estados(self):
        return tuple(self.__estados)


class Fabrica:

    def __init__(self, nome):
        self.nome = nome

    def estado(self):
        return Estado(Fabrica(self.nome))

    def restaura(self, estado):
        self.nome = estado.estado.nome

if __name__ == '__main__':
    historico = Historico()

    fabrica = Fabrica('Nome 1')
    historico += fabrica.estado()

    fabrica.nome = 'Nome 2'
    historico += fabrica.estado()

    fabrica.nome = 'Nome 3'
    historico += fabrica.estado()

    print(historico.estados)

    fabrica.restaura(historico(0))
    historico += fabrica.estado()

    print(fabrica.nome)