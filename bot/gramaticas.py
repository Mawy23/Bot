# usr/bin/python3

import random

# Definición de la gramática
gramatica = {
    "<titulo>": ["<sujeto> <verbo> <complemento>"],
    "<sujeto>": ["Fernando Alonso", "El piloto español", "El asturiano"],
    "<verbo>": ["gana", "pierde", "sorprende en", "se retira de"],
    "<complemento>": ["el Gran premio de Mónaco", "la última carrera", "la clasificación"]
}

def generar_frase(simbolo="<titulo>"):
    """Genera una frase a partir de un simbolo no terminal utilizando la gramática definida."""
    if(simbolo not in gramatica):
        return simbolo
    
    # Seleccionar una producción aleatoria para el simbolo
    produccion = random.choice(gramatica[simbolo])
    # Dividir la producción en sus componentes y generar la frase para cada componente
    
    return " ".join([generar_frase(comp) for comp in produccion.split()])