from .Productos import Producto
from .config.archivos import Directorio

class VentaProductos:

    def __init__(self):
        self._Cesta_Venta=[]

    def __srt__(self):
        return self._Cesta_Venta

    @property
    def getcesta_venta(self):
        if len(self._Cesta_Venta):
            return self._Cesta_Venta

    def AgregarVenta(self):
        #arreglar
        if self.producto.Verficarproducto(self.producto.getNproduct):
            pass
#       (vproducto)*12/100
            #     pv=float(i['PrecioCompra'])*12/100
            #     self._Cesta_Venta.append({'producto': self.producto.getNproduct,'Cantidad':cantidad,'PV':str(pv)})
            # return True

    def json(self):
        import time
        dicts={
               'Venta N°:':0,
               'Fecha:':time.strftime("%d/%m/%y"),
               'Cliente:':'carlos',
               'lista de productos':self._Cesta_Venta,
               }         
        p=[]
        r=[]
        subtotal=0
        total=0
        [p.append(tuple((str(i),dicts[i]))) for i in dicts ]
        for i,e in p:
            if type(e) is list:
                for t in e:
                    r.append("Producto: {0} Cantidad {1} Precio.U: {2:.2f} ".format(t['producto'],t['Cantidad'],float(t['PV'])))
            if type(e) is not list:
                r.append(str(str(i)+str(e)))
        return r
        
    def _guargar_txt(self):
        with open( Directorio()+'\\Ventas','a') as archivo:
            archivo.write('*'*100+'\n')
            for i in self.json():
                archivo.write(i+'\n')
            archivo.write('*'*100+'\n')
    
    def verCesta(self):
        print('La cesta Actualmente contiene los siguientes Productos:')
        for i in self._Cesta_Venta:
                print(f"Producto:{i['producto']} PV:{i['PV']}")

    def BuscarProducto(self,buscar):
        contenedor=[]
        for i in self.Objcompra.getcesta:
            if buscar in i['Producto']:
                contenedor.append(i)
        return contenedor

obVEn=VentaProductos()
