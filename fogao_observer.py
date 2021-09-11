from estado import EstadoFogao


class FogaoUnico(type):

    _fogao_unico = None

    def __call__(cls):
        if not cls._fogao_unico:
            cls._fogao_unico = super().__call__()

        return cls._fogao_unico


class Fogao(metaclass=FogaoUnico):

    def __init__(self):
        self.__estado = EstadoFogao.DESLIGADO
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

    def ligar(self):
        self.__estado = EstadoFogao.LIGADO
        self.notificar(evento=self.__estado)

    def desligar(self):
        self.__estado = EstadoFogao.DESLIGADO
        self.notificar(evento=self.__estado)


fogao = Fogao()
