import estado
import evento
from mundofisico import mundo_fisico


class Frigideira:

    def __init__(self, mediador=mundo_fisico):
        self.__estado = estado.Frigideira.FRIA
        self.__mediador = mediador

    def aquecer(self):
        self.__estado = estado.Frigideira.QUENTE
        self.__transferir_calor()

    def esfriar(self):
        self.__estado = estado.Frigideira.FRIA
        self.__interromper_calor()

    def __transferir_calor(self):
        self.__mediador.notificar(
            evento=evento.Frigideira.TRANSFERIR_CALOR,
            utensilio=self,
        )

    def __interromper_calor(self):
        self.__mediador.notificar(
            evento=evento.Frigideira.INTERROMPER_CALOR,
            utensilio=self,
        )


class Espatula:

    @classmethod
    def mexer(self, utensilio):
        for ingrediente in utensilio.ingredientes():
            ingrediente.mexer()


frigideira = Frigideira()
