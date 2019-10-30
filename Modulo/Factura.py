from .Cliente import Clientes
from .Ventas import VentaProductos

class factura:

  __iva=12 
  
  def __init__(self,CodigoCliente):
    
    self.codigo=4444
    self.serie=3333
    self.obj_cliente=Clientes(CodigoCliente)
    self.Obj_venta=VentaProductos()

  def __str__(self):
    return f'{self.codigo},{self.serie} {self.obj_cliente.get_Nombre} {self.Obj_venta._Cesta_Venta}'
 
  def getCabecera(self,nombreE):
        print ('''
          Factura : {0}  codigo: {1}  serie: {2} 
          +++++++++++++++++++++++++++++++++++++
          cliente: {3} Cedula: None CodCliente: {4}'''.format(
           nombreE,
           self.codigo,
           self.serie,
           str(self.obj_cliente.get_Nombre+' '+self.obj_cliente.get_Apellido),
           self.obj_cliente.get_Codigo
          ) 
          )
 
  def getdetalle(self):         

         total=0
         subtotal=0

         print('''
         {:^10} {:^10} {:^10}'''.format('Descripcion','Cantidad','Precio.U'))
         for i in self.Obj_venta.getcesta_venta:   
           valor=float(i['PV'])*float(i['Cantidad'])
           print('''
           {:^10} {:^10} {:^10}'''.format(i['producto'], i['Cantidad'],i['PV']))
           subtotal+=float(valor)
           total=subtotal+float(self.__iva*subtotal/100)
         print('''
         ................Subtotal: {0:.2f}'''.format(subtotal))   
         print('''
         ....................Iva:   {0:.2f}'''.format(self.__iva*subtotal/100))

         print('''
         ...................total: {0:.2f}'''.format(total))
      
  def generarFactura(self,nombreE):
        self.getCabecera(nombreE)
        self.getdetalle()
