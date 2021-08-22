from enum import Enum


class EstadoCasca(Enum):
    INTEIRA = 'inteira'
    QUEBRADA = 'quebrada'


class EstadoClara(Enum):
    TRANSPARENTE = 'transparente'
    BRANCA = 'branca'


class EstadoGema:
    LIQUIDA = 'liquida'
    PASTOSA = 'pastosa'
    SOLIDA = 'solida'


class Ovo:

    def __init__(self):
        self.__estado = {
            'casca': EstadoCasca.INTEIRA,
            'clara': EstadoClara.BRANCA,
            'gema': EstadoGema.LIQUIDA,
            'mexido': True,
        }

    def quebrar_casca(self):
        self.__estado['casca'] = EstadoCasca.QUEBRADA

    def estado_clara(self):
        return self.__estado['clara']

    def estado_gema(self):
        return self.__estado['gema']

    def estado_ovo(self):
        return self.__estado

    def mexer(self):
        self.__estado['mexido'] = True


class OleoVegetal:

    def __init__(self):
        pass
