import erros
from estado import EstadoFogao
import evento
from mundofisico import mundo_fisico


class FogaoUnico(type):

    _fogao_unico = None

    def __call__(cls):
        if not cls._fogao_unico:
            cls._fogao_unico = super().__call__()

        return cls._fogao_unico


class Fogao(metaclass=FogaoUnico):

    def __init__(self, mediador=mundo_fisico):
        self.__estado = EstadoFogao.DESLIGADO
        self.__mediador = mediador

    def ligar(self):
        self.__estado = EstadoFogao.LIGADO
        self.__mediador.notificar(
            evento=evento.Fogao.LIGAR,
            fogao=self,
        )

    def desligar(self):
        self.__estado = EstadoFogao.DESLIGADO
        self.__mediador.notificar(
            evento=evento.Fogao.DESLIGAR,
            fogao=self,
        )


fogao = Fogao()
