from fogao import fogao
from ingredientes import OleoVegetal, Ovo
from mundofisico import (
    mundo_fisico,
    EventoFrigideira,
    EventoIngrediente,
)
from utensilios import Frigideira


# Preparar Ingredientes
oleo = OleoVegetal()
ovo1 = Ovo()
ovo2 = Ovo()
ovo3 = Ovo()

# Pegar a Frigideira
frigideira = Frigideira()

# Colocar a Frigideira no Fogão
mundo_fisico.notificar(
    evento=EventoFrigideira.COLOCAR_NO_FOGAO,
    fogao=fogao,
    utensilio=frigideira,
)

# Colocar os Ingredientes na Frigideira
mundo_fisico.notificar(
    evento=EventoIngrediente.COLOCAR_NA_FRIGIDEIRA,
    ingredientes=[
        oleo,
        ovo1.quebrar_casca(),
        ovo2.quebrar_casca(),
        ovo3.quebrar_casca(),
    ],
    utensilio=frigideira,
)

fogao.ligar()
