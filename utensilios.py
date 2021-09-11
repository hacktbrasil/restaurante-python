from enum import Enum

from mundofisico_mediator import mundo_fisico, EventoFrigideira


class Frigideira:

    def __init__(self):
        self.__ingredientes = []

    def aquecer(self):
        self.transferir_calor()

    def esfriar(self):
        pass

    def transferir_calor(self):
        for ingrediente in self.__ingredientes:
            ingrediente.fritar()

    def adicionar_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)

    def remover_ingrediente(self, ingrediente):
        self.__ingredientes.remove(ingrediente)


class Espatula:

    @classmethod
    def mexer(self, utensilio):
        for ingrediente in utensilio.ingredientes():
            ingrediente.mexer()


frigideira = Frigideira()
