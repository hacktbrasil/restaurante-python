from enum import Enum


class Temperatura(Enum):
    AMBIENTE = 'ambiente'
    BAIXA = 'baixa'
    MEDIA = 'media'
    ALTA = 'alta'


class Frigideira:

    def __init__(self):
        self.__ingredientes = []
        self.__temperatura = Temperatura.AMBIENTE

    def adicionar_ingrediente(self, ingrediente):
        self.__ingredientes.append(ingrediente)
        print(f'{ingrediente} foi adicionado à frigideira')

    def estado_ingredientes(self):
        pass


class Espatula:

    @classmethod
    def mexer(self, utensilio):
        for ingrediente in utensilio.ingredientes():
            ingrediente.mexer()


frigideira = Frigideira()
