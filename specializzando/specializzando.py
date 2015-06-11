
class specializzando:

    def __init__(self, nome, cognome, CF, sesso, anno_iscrizione, neo, mat,):
        self.nome = nome
        self.cognome = cognome
        self.CF = CF
        self.sesso = sesso
        self.anno_iscrizione = anno_iscrizione
        self.neo = neo
        self.mat = mat
        self.desiderata = {}

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome

    def getCF(self):
        return self.CF

    def getSesso(self):
        return self.sesso

    def getAnnoIscrizione(self):
        return self.anno_iscrizione

    def getNeo(self):
        return self.neo

    def getMat(self):
        return self.mat

    def addDesiderata(self, data, tipoDesiderata):
        # desiderata[metti la chiave] = metti il valore nuovi
        self.desiderata[data] = tipoDesiderata

    def remDesiderata(self, data):
        if data is self.desiderata.keys():
            del self.desiderata[data]

    def getDesiderata(self):
        return self.desiderata

    def clearDesiderata(self):
        self.desiderata.clear()
