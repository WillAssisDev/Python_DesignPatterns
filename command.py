from abc import ABCMeta, abstractmethod


class Comando(metaclass=ABCMeta):

    @abstractmethod
    def executa(self):
        pass


class Comando1(Comando):

    def executa(self):
        print('Comando 1')


class Comando2(Comando):

    def executa(self):
        print('Comando 2')


class FilaDeTrabalho:

    def __init__(self):
        self.__comandos = []

    def __iadd__(self, comando):
        self.__comandos.append(comando)
        return self

    def processa(self):
        for comando in self.__comandos:
            comando.executa(self)


if __name__ == '__main__':
    fila = FilaDeTrabalho()

    comando_1 = Comando1
    fila += comando_1

    comando_2 = Comando2
    fila += comando_2

    fila.processa()