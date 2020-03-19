def decorador(metodo_ou_funcao):

    def empacotador(self):
        return metodo_ou_funcao(self) + 1

    return empacotador


class Dez:

    def __init__(self):
        self.dez = 10

    @decorador
    def mostra(self):
        return self.dez


if __name__ == '__main__':
    dez = Dez()
    print(dez.mostra())