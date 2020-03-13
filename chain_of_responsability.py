class Responsabilidade1:

    def __init__(self, proxima_responsabilidade):
        self.proxima_responsabilidade = proxima_responsabilidade

    def funcao(self, parametro1, parametro2):
        if parametro1:
            print('Responsabilidade 1')
        else:
            return self.proxima_responsabilidade.funcao(parametro1, parametro2)


class Responsabilidade2:

    def __init__(self, proxima_responsabilidade):
        self.proxima_responsabilidade = proxima_responsabilidade

    def funcao(self, parametro1, parametro2):
        if parametro2:
            print('Responsabilidade 2')
        else:
            return self.proxima_responsabilidade.funcao(parametro1, parametro2)


class ResponsabilidadeNenhuma:

    def funcao(self, parametro1=None, parametro2=None):
        pass


class Fabrica:

    def ordenar_responsabilidades(self, parametro1, parametro2):
        Responsabilidade1(
            Responsabilidade2(
                ResponsabilidadeNenhuma()
            )
        ).funcao(parametro1, parametro2)


if __name__ == '__main__':
    fabrica = Fabrica()
    fabrica.ordenar_responsabilidades(True, False)
    fabrica.ordenar_responsabilidades(False, True)
    fabrica.ordenar_responsabilidades(False, False)
