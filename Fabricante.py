

class Fabricante:
    def __init__(self):
        self.idLaboratorio = None
        self.nombreLaboratorio = None
        self.dirección = None
        self.estado = None
        self.emailContacto = None
        self.telefonoContacto = None


    def setId(self, idL):
        self.idLaboratorio = idL

    def getId(self):
        return self.idLaboratorio

    def setNombre(self, nombre):
        self.nombreLaboratorio = nombre

    def getNombre(self):
        return self.nombreLaboratorio

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setEstado(self, estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

    def setEmail(self, email):
        self.emailContacto = email

    def getEmail(self):
        return self.emailContacto

    def setTelefono(self, tel):
        self.telefonoContacto = tel

    def getTelefono(self):
        return self.telefonoContacto

