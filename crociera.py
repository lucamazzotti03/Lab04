from cabine import Cabina
from cabine import CabinaDeluxe
from cabine import Passeggero
import operator

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.cabine = []
        self.passeggeri = []

    def __str__(self):
        return f"{self._nome}"

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
                            cabina = Cabina(riga[0], riga[1], riga[2], riga[3], "-")
                            self.cabine.append(cabina)
                        elif len(riga) > 4 and riga[4].isdigit():
                            prezzo = float(int(riga[3])*(1 + 0.1*int(riga[4])))
                            cabina = Cabina(riga[0], riga[1], riga[2], prezzo, riga[4])
                            self.cabine.append(cabina)

                        elif len(riga) > 4 and riga[4].isalnum():
                            prezzo = float(int(riga[3])*1.2)
                            cabina = CabinaDeluxe(riga[0], riga[1], riga[2], prezzo, riga[4])
                            self.cabine.append(cabina)

                    elif riga[0][0] == "P":
                        passeggero = Passeggero(riga[0], riga[1], riga[2])
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
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        return sorted(self.cabine, key = operator.attrgetter("prezzo"))
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

