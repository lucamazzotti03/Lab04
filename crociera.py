from cabine import Cabina
from cabine import CabinaDeluxe
from cabine import Passeggero
import operator

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.cabine = []
        self.passeggeri = []
        self.assegnazionicabine = []

    def __str__(self):
        return f"{self._nome}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        if not isinstance(nuovo_nome, str):
            raise TypeError("Il nome della crociera deve essere una stringa")
        self._nome = nuovo_nome
        print(f"Nuovo nome della Crociera:{self._nome}")

    """Inizializza gli attributi e le strutture dati"""
    # TODO

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for riga in file:
                    riga = riga.rstrip().split(",")
                    if riga[0][:3] == "CAB":
                        if len(riga) == 4:
                            cabina = Cabina(riga[0], riga[1], riga[2], riga[3], "0", "disponibile")
                            self.cabine.append(cabina)
                        elif len(riga) > 4 and riga[4].isdigit():
                            prezzo = float(int(riga[3])*(1 + 0.1*int(riga[4])))
                            cabina = Cabina(riga[0], riga[1], riga[2], prezzo, riga[4], "disponibile")
                            self.cabine.append(cabina)

                        elif len(riga) > 4 and riga[4].isalnum():
                            prezzo = float(int(riga[3])*1.2)
                            cabina = CabinaDeluxe(riga[0], riga[1], riga[2], prezzo, riga[4], "disponibile")
                            self.cabine.append(cabina)

                    elif riga[0][0] == "P":
                        passeggero = Passeggero(riga[0], riga[1], riga[2], "")
                        self.passeggeri.append(passeggero)

            for c in self.cabine:
                print(c)
            for p in self.passeggeri:
                print(p)

        except FileNotFoundError:
            print("File non trovato")

        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):

        cabineDisponibili = []
        for cabina in self.cabine:
            cabineDisponibili.append(cabina.codice)
        if codice_cabina not in cabineDisponibili:
            raise Exception("Cabina non disponibile")

        passeggeriDisponibili = []
        for passeggero in self.passeggeri:
            passeggeriDisponibili.append(passeggero.codice)
        if codice_passeggero not in passeggeriDisponibili:
            raise Exception("Passeggero non disponibile")

        for cabina in self.cabine:
            if cabina.codice == codice_cabina:
                self.cabine.remove(cabina)


        for passeggero in self.passeggeri:
            if passeggero.codice == codice_passeggero:
                passeggero.cabina = codice_cabina
                self.assegnazionicabine.append(passeggero)
                self.passeggeri.remove(passeggero)

        return True


        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        return sorted(self.cabine, key = operator.attrgetter("prezzo"))
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        for passeggerocabina in self.assegnazionicabine:
            print(passeggerocabina)
        for passeggero in self.passeggeri:
            print(passeggero)


        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

