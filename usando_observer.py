from fogao import fogao
from ingredientes import OleoVegetal, Ovo
from utensilios_observer import Frigideira


# Preparar Ingredientes
oleo = OleoVegetal()
ovo1 = Ovo()
ovo2 = Ovo()
ovo3 = Ovo()

# Pegar a Frigideira
frigideira = Frigideira()

# Colocar Frigideira no Fogão
fogao.inscrever(frigideira)

# Colocar Ingredientes na Frigideira
ingredientes = [
    oleo,
    ovo1.quebrar_casca(),
    ovo2.quebrar_casca(),
    ovo3.quebrar_casca(),
]
for ingrediente in ingredientes:
    frigideira.inscrever(ingrediente)

fogao.ligar()
