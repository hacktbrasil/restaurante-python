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
            'clara': EstadoClara.TRANSPARENTE,
            'gema': EstadoGema.LIQUIDA,
            'mexido': True,
        }

    def quebrar_casca(self):
        self.__estado['casca'] = EstadoCasca.QUEBRADA
        return self

    def estado_clara(self):
        return self.__estado['clara']

    def estado_gema(self):
        return self.__estado['gema']

    def estado_ovo(self):
        return self.__estado

    def mexer(self):
        self.__estado['mexido'] = True
    
    def fritar(self):
        self.__estado['clara'] = EstadoClara.BRANCA

        if self.__estado['gema'] == EstadoGema.LIQUIDA:
            self.__estado['gema'] = EstadoGema.PASTOSA

        elif self.__estado['gema'] == EstadoGema.PASTOSA:
            self.__estado['gema'] = EstadoGema.SOLIDA


class OleoVegetal:

    def __init__(self):
        pass
