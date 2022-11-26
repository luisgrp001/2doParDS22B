
class ViasAdministracion:
    def __init__(self):
        self.idViaAdmin = None
        self.viaAdministracion = None
        self.descripciónDeAplicacion = None

    def setid(self, idp):
        self.idViaAdmin = idp

    def getid(self):
    	return self.idViaAdmin

    def setviaAdmin(self, via):
        self.viaAdministración = via

    def getviaAdmin(self):
        return self.viaAdministración

    def setDescripcion(self, desc):
        self.descripciónDeAplicación = desc

    def getDescripcion(self, ):
        return self.descripciónDeAplicación