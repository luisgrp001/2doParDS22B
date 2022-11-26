from Fabricante import Fabricante
from Medicamento import Medicamento
from Pais import Pais
from ViasAdministracion import ViasAdministracion

mexico = Pais()
mexico.idPais = 1
mexico.nombrePais = "Mexico"

print("ID Pais: ",mexico.idPais,"\nNombre País:",mexico.nombrePais)

penicilina = Medicamento()
penicilina.codigo = 1
penicilina.nombreActivo = "Penicilina"
penicilina.dci = "PenicinActive"
penicilina.presentacion = "Soluble"
penicilina.tipoGenPat = "Patente"
penicilina.fechaFabricacion = "20/11/2022"
penicilina.fechaCaducidad = "20/11/2025"

print("-----------MEDICAMENTO--------------")
print("Cod",penicilina.codigo,"\nNombre: ",penicilina.nombreActivo,"\nDCI: ",penicilina.dci,"\nPresentacion: ",penicilina.presentacion,"\nTipo: ",penicilina.tipoGenPat,"\nFechaf: ",penicilina.fechaFabricacion,"\nFecha Cad: ",penicilina.fechaCaducidad)