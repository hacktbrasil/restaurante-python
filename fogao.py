import erros
from estado import EstadoFogao


class Singleton(type):

    _instancias = {}

    def __call__(cls):
        if not cls in cls._instancias.keys():
            cls._instancias[cls] = super().__call__()

        return cls._instancias[cls]


class Fogao(metaclass=Singleton):

    def __init__(self):
        self.__estado = EstadoFogao.DESLIGADO
        self.__utensilio_na_trempe = None

    def ligar(self):
        self.__estado = EstadoFogao.LIGADO
        self.__utensilio_na_trempe.aquecer()

    def desligar(self):
        self.__estado = EstadoFogao.DESLIGADO
        self.__utensilio_na_trempe.esfriar()

    def colocar_utensilio(self, utensilio):
        if self.__utensilio_na_trempe is not None:
            raise erros.TrempeCheia()

        self.__utensilio_na_trempe = utensilio

    def retirar_utensilio(self):
        self.__utensilio_na_trempe = None


fogao = Fogao()
