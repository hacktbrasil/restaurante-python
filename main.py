import time

from energia import IntensidadeCalor
from fogao import fogao, Fogao
from ingredientes import OleoVegetal, Ovo
from utensilios import Espatula
import armario


def cozinheiro():
    fazer_ovos_mexidos(
        fogao=fogao,
        
    )


def fazer_ovos_mexidos(fogao, frigideira, espatula, ovos, oleo):
    oleo_vegetal = OleoVegetal()

    frigideira.adicionar_ingrediente(oleo_vegetal)

    for ovo in ovos:
        ovo.quebrar_casca()
        frigideira.adicionar_ingrediente(ovo)

    fogao.colocar_utensilio(frigideira)

    fogao.ajustar_intensidade(IntensidadeCalor.FOGO_MEDIO)

    Espatula.mexer(utensilio=frigideira)

    while not ovos_mexidos_prontos(frigideira.estado_ingredientes()):
        time.sleep(5)

    fogao.desligar

    return frigideira.ingredientes()


def ovos_mexidos_prontos(estado_ingredientes):
    for ingrediente in estado_ingredientes:
        pass
