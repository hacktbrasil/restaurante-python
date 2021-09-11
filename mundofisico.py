from enum import Enum

import evento


class MundoFisico:

    def __init__(self):
        self.__mediadores = {
            evento.Fogao.LIGAR: self.notificar_fogao_ligado,
            evento.Fogao.DESLIGAR: self.notificar_fogao_desligado,
            evento.Frigideira.COLOCAR_NO_FOGAO: self.colocar_utensilio_fogao,
            evento.Frigideira.RETIRAR_DO_FOGAO: self.retirar_utensilio_fogao,
            evento.Frigideira.TRANSFERIR_CALOR: self.frigideira_aquecendo,
            evento.Ingrediente.COLOCAR_NA_FRIGIDEIRA: self.colocar_ingrediente,
            evento.Ingrediente.RETIRAR_DA_FRIGIDEIRA: self.retirar_ingrediente,
        }

        self.utensilio_no_fogao = {}
        self.ingrediente_no_utensilio = {}

    def notificar(self, evento, *args, **kwargs):
        if evento not in self.__mediadores.keys():
            raise ValueError(f'Evento não suportado pelo mediador: "{evento}"')

        mediador = self.__mediadores[evento]
        mediador(*args, **kwargs)

    def notificar_fogao_ligado(self, fogao):
        utensilio = self.utensilio_no_fogao.get(fogao, None)

        if utensilio is not None:
            return utensilio.aquecer()

    def notificar_fogao_desligado(self, fogao):
        pass

    def colocar_utensilio_fogao(self, fogao, utensilio):
        self.utensilio_no_fogao[fogao] = utensilio

    def retirar_utensilio_fogao(self, fogao, utensilio=None):
        self.utensilio_no_fogao[fogao] = None

    def frigideira_aquecendo(self, utensilio):
        if self.frigideira_tem_oleo():
            for ingrediente in self.ingrediente_no_utensilio[utensilio]:
                ingrediente.fritar()

        elif self.frigideira_tem_agua():
            for ingrediente in self.ingrediente_no_utensilio[utensilio]:
                ingrediente.cozinhar()

    def frigideira_tem_oleo():
        pass

    def frigideira_tem_agua():
        pass

    def colocar_ingrediente(self, utensilio, ingredientes):
        if utensilio not in self.ingrediente_no_utensilio.keys():
            self.ingrediente_no_utensilio[utensilio] = []

        self.ingrediente_no_utensilio[utensilio].append(ingredientes)

    def retirar_ingrediente(self, utensilio, ingrediente):
        self.ingrediente_no_utensilio[utensilio].remove(ingrediente)


mundo_fisico = MundoFisico()
