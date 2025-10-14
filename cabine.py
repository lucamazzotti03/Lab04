from encodings import normalize_encoding


class Cabina:
    def __init__(self, codice, letti, ponte, prezzo, animali):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.animali = animali

    def __str__(self):
        return (f"{self.codice} letti:{self.letti}, ponte:{self.ponte}, "
                f"prezzo:{self.prezzo}, animali:{self.animali}")

class CabinaDeluxe:
    def __init__(self, codice, letti, ponte, prezzo, tipo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.tipo = tipo
    def __str__(self):
        return (f"{self.codice} letti:{self.letti}, ponte:{self.ponte}, "
                f"prezzo:{self.prezzo}, tipo:{self.tipo}")

class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
    def __str__(self):
        return f"codice:{self.codice}, nome:{self.nome} {self.cognome}"