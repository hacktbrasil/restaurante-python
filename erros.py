
class ErroCozinha(Exception):
    pass


class ErroFogao(ErroCozinha):
    pass


class TrempeCheia(ErroFogao):
    pass
