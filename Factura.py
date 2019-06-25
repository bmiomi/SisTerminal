from Ventas import VentaProductos

class factura(VentaProductos):
       __iva=12 

       def __init__(self,codigo,serie,numero):
             self.codigo=codigo
             self.serie=serie
             self.numero=numero

       def getnumero(self):
             if self.codigo is None:
                   return 'no sea asignado un numero que identifique la factura'
             return 'numbero {}'.format(self.numero)
    
       def getserie(self):
         if self.serie is None:
           return 'no sea asignado una serie que identifique la factura'
         return 'serie {}'.format(self.serie)
       
       def getcodigo(self):
         if self.codigo is None:
           return 'no sea asignado un codigo que identifique la factura'
         return 'codigo {}'.format(self.codigo)  
       
       def getCabecera(self,cliente):
           print('''
           Factura : {0}   codigo: {1}  serie: {2} 
           +++++++++++++++++++++++++++++++++++++
           cliente: {3}'''.format(self.numero,self.codigo,self.serie,cliente))
           return'      +++++++++++++++++++++++++++++++++++++'
       
       def getdetalle(self):
             Cproduct=self.getcesta_ventas
             total=0
             print('''
             {:^10} {:^10}'''.format('Descripcion','Precio'))
             for i in Cproduct:   
               a=i['producto']
               b=i['PV']
               ##c=i['Cantidad']
               print('''
               {:^10} {:^10}'''.format(i['producto'], i['PV']))
               subtotal=1*int(float(b))
               total+=subtotal
             print('''
             ................................''')   
             print('''
             ...................total: {0}'''.format(total))
