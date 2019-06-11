from Factura import factura

class Empresa(factura):

  def __init__(self,nombreE,codigo,serie,numero):
    super().__init__(codigo,serie,numero)
    self.Nombre=nombreE

  def generarfactura(self,cliente,cantidad,precio):
      return self.getfactura(cliente,cantidad,precio)
