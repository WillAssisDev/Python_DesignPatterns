from abc import ABCMeta, abstractmethod


class Template:
    __metaclass__ = ABCMeta

    def funcao(self, parametro1):
        if self.verificacao(parametro1):
            return self.retorno1(parametro1)
        else:
            return self.retorno2(parametro1)

    @abstractmethod
    def verificacao(self, parametro1):
        pass

    @abstractmethod
    def retorno1(self, parametro1):
        pass

    @abstractmethod
    def retorno2(self, parametro1):
        pass


class Classe1(Template):

    def verificacao(self, parametro1):
        return True if parametro1 else False

    def retorno1(self, parametro1):
        print('Retorno 1')

    def retorno2(self, parametro1):
        print('Retorno 2')


class Fabrica:

    def fabricar(self, parametro1):
        classe = Classe1()
        classe.funcao(parametro1)


if __name__ == '__main__':
    fabrica = Fabrica()
    fabrica.fabricar(True)
    fabrica.fabricar(False)