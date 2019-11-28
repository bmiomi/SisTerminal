#usr/bin/UFT-8
from .Compra import Compras
from .config.archivos import Directorio

class VentaProductos:

    _Cesta_Venta=[]

    def __init__(self):
        self.Objcompra=Compras()

    @property
    def getcesta_venta(self):
        return self._Cesta_Venta

    def AgregarVenta(self,producto,cantidad):
        elemento=self.BuscarProducto(producto)
        if len (elemento)!=0:
            elemento[-1]
        elif len(elemento)==1:
            elemento
        else:
            print(f'No existe registro del producto {producto}')
            return False

        for i in elemento:
            if producto in i['Producto']:
                pv=float(i['PrecioCompra'])*12/100
                self._Cesta_Venta.append({'producto': producto,'Cantidad':cantidad,'PV':str(pv)})
                return True

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
