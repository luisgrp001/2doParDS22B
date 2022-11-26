
class Medicamento:
    def __init__(self):
        self.codigo = None
        self.nombreActivo = None
        self.dci = None
        self.presentacion = None
        self.tipoGenPat = None
        self.fechaFabricacion = None
        self.fechaCaducidad = None

    def setCod(self, cod):
        self.codigo = cod

    def getCod(self):
        return self.codigo

    def setNom(self, nomb):
        self.nombreActivo = nomb

    def getNom(self):
        return self.nombreActivo

    def setDCI(self, dcin):
        self.dci = dcin

    def getDCI(self):
        return self.dci

    def setPresentacion(self, pres):
        self.presentacion = pres

    def getPresentacion(self):
        return self.presentacion

    def setTipo(self, tipo):
        self.tipoGenPat = tipo

    def getTipo(self):
        return self.tipoGenPat

    def setFechaF(self, fecha):
        self.fechaFabricacion = fecha

    def getFechaF(self):
        return self.fechaFabricacion

    def setFechaCad(self, fecha):
        self.fechaCaducidad = fecha

    def getFechaCad(self):
        return self.fechaCaducidad