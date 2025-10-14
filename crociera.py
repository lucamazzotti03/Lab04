from cabine import Cabina


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
                        if len(riga) > 4 and riga[4].isdigit():
                            cabina = Cabina(riga[0], riga[1], riga[2], riga[3], riga[4], "-")
                            self.cabine.append(cabina)

                        elif len(riga) > 4 and riga[4].isalnum():
                            animali = "-"
                            tipo = riga[4]
                            cabina = Cabina(codice, letti, ponte, prezzo, animali, tipo)
                            self.cabine.append(cabina)

                    elif riga[0][0] == "P":
                        passeggero = {"codice" : riga[0],
                                      "nome" : riga[1],
                                      "cognome" : riga[2]}
                        self.passeggeri.append(passeggero)

            print(Cabina.__str__(self))
        except FileNotFoundError:
            print("File non trovato")

        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

