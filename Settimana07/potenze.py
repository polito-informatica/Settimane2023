

def potenza(base, esponente):

    return base ** esponente

def cubo(lato):
    """Funzione per calcolare il volume di un cubo, dato il lato

    Args:
        lato (float): lunghezza del lato

    Returns:
        float: valore del volume
    """
    return potenza(lato, 3)

def quadrato(lato):
    return potenza(lato, 2)

print(cubo(5))

print(quadrato(4))