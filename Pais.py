
class Pais:
    def __init__(self):
        """
        Initialize teh object

        Args:
            self (Pais): the object
        """
        self.idPais = None
        self.nombrePais = None

    def setidPais(self, idPais):
        """
        Introduce the value for Id

        Args:
            self (Pais): the object
            idPais (int): the value of Id
        """
        self.idPais = idPais

    def getidPais(self):
        """
        Get the value of Id

        Args:
            self (Pais): the object

        Returns:
            self.idPais (int): the value contained for this object
        """
        return self.idPais

    def setnomPais(self, pais):
        """
        Set the name of country

        Args:
            self (Pais): the object

        """
        self.nombrePais = pais

    def getnomPais(self):
        """
        Get the value of name

        Args:
            self (Pais): the object

        Returns:
            self.nombrePais (str): the name of country
        """
        return self.nombrePais