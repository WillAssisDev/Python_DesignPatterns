class Estrategia1:

    def funcao(self, parametro1):
        if parametro1:
            print('Estratégia 1')


class Estrategia2:

    def funcao(self, parametro1):
        if parametro1:
            print('Estratégia 2')

class Estrategia3:

    def funcao(self, parametro1):
        if parametro1:
            print('Estratégia 3')


class Fabrica:

    def fabricar(self, estrategia, parametro1):
        estrategia.funcao(parametro1) # duck typing


if __name__ == '__main__':
    fabrica = Fabrica()
    fabrica.fabricar(Estrategia1(), True)
    fabrica.fabricar(Estrategia1(), False)
    fabrica.fabricar(Estrategia2(), True)
    fabrica.fabricar(Estrategia2(), False)
    fabrica.fabricar(Estrategia3(), False)
    fabrica.fabricar(Estrategia3(), True)
