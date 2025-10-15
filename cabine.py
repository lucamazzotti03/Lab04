from encodings import normalize_encoding


class Cabina:
    def __init__(self, codice, letti, ponte, prezzo, animali, stato):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.animali = animali
        self.stato = stato

    def __str__(self):
        return f"{self.codice} | {self.letti} letti - ponte {self.ponte} - prezzo {self.prezzo}€ - Max animali: {self.animali} - {self.stato}"


class CabinaDeluxe:
    def __init__(self, codice, letti, ponte, prezzo, tipo, stato):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = float(prezzo)
        self.tipo = tipo
        self.stato = stato
    def __str__(self):
        return f"{self.codice} | {self.letti} letti - ponte {self.ponte} - prezzo {self.prezzo}€ - Tipo: {self.tipo} - {self.stato}"

class Passeggero:
    def __init__(self, codice, nome, cognome, cabina):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.cabina = cabina
    def __str__(self):
        return f"codice:{self.codice}, nome:{self.nome} {self.cognome} - CABINA: {self.cabina}"