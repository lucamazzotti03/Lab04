class Cabina:
    def __init__(self, codice, letti, ponte, prezzo, animali, tipo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.animali = animali
        self.tipo = tipo

    def __str__(self):
        return (f"{self.codice} letti:{self.letti}, ponte:{self.ponte}, "
                f"prezzo:{self.prezzo}, animali:{self.animali}, tipo:{self.tipo}")