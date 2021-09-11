import estado


class Frigideira:

    def __init__(self):
        self.__estado = estado.Frigideira.FRIA
        self.__observadores = []

    def inscrever(self, observador):
        if observador not in self.__observadores:
            self.__observadores.append(observador)

    def desinscrever(self, observador):
        if observador in self.__observadores:
            self.__observadores.remove(observador)

    def notificar(self, evento):
        for observador in self.__observadores:
            observador.atualizar(origem=self, evento=evento)

    def atualizar(self, origem, evento):
        if evento == estado.Fogao.LIGADO:
            self.aquecer()

        elif evento == estado.Fogao.DESLIGADO:
            self.esfriar()

    def aquecer(self):
        self.__estado = estado.Frigideira.QUENTE
        self.__transferir_calor()

    def esfriar(self):
        self.__estado = estado.Frigideira.FRIA
        self.__interromper_calor()

    def __transferir_calor(self):
        if self.__estado == estado.Frigideira.FRIA:
            self.notificar(evento=estado.Frigideira.QUENTE)

    def __interromper_calor(self):
        if self.__estado == estado.Frigideira.QUENTE:
            self.notificar(evento=estado.Frigideira.FRIA)


class Espatula:

    @classmethod
    def mexer(self, utensilio):
        for ingrediente in utensilio.ingredientes():
            ingrediente.mexer()


frigideira = Frigideira()
