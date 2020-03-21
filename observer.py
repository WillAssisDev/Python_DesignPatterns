def funcao_observadora_1():
    print('Função 1')

def funcao_observadora_2():
    print('Função 2')


class Fabrica:

    def __init__(self, observadores):
        for observador in observadores:
            observador()


if __name__ == '__main__':
    fabrica = Fabrica([funcao_observadora_1, funcao_observadora_2])