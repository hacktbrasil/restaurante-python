from enum import Enum

import erros
from energia import IntensidadeCalor


class EstadoFogao:
    DESLIGADO = 'desligado'
    LIGADO = 'ligado'


class Fogao:

    def __init__(self):
        self.__estado = EstadoFogao.DESLIGADO
        self.__intensidade_calor = IntensidadeCalor.AMBIENTE
        self.__utensilio_na_trempe = None

    def ajustar_intensidade(self, intensidade):
        if not isinstance(intensidade, IntensidadeCalor):
            raise TypeError('Intensidade do fogo inválida')

        elif intensidade == IntensidadeCalor.DESLIGADO:
            self.desligar()

        else:
            self.__estado = intensidade

    def desligar(self):
        self.__estado = IntensidadeCalor.DESLIGADO

    def estado(self):
        return self.__estado

    def colocar_utensilio(self, utensilio):
        if self.__utensilio_na_trempe is not None:
            raise erros.TrempeCheia()

        self.__utensilio_na_trempe = utensilio

    def retirar_utensilio(self):
        self.__utensilio_na_trempe = None


fogao = Fogao()
