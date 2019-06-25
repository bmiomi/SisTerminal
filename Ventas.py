from Compra import Compras
from archivos import CrearDirectorio
ar=CrearDirectorio()
class VentaProductos(Compras):
    
    _Cesta_Venta=[]

    @property
    def getcesta_ventas(self):
        return self._Cesta_Venta

    def __buscarProducto(self,Nproduct):
        x=self.setc()
        for i in x:
            if Nproduct in i.values():
                return i,True
        return {},False

    def Agregar_Venta(self,producto):
        i,r=self.__buscarProducto(producto)
        if  producto in i.values():
            pv=float(i['PrecioCompra'])*12/100
            self._Cesta_Venta.append({'producto': producto,'PV':str(pv)})
            print('Producto agregado a la Cesta.')
        else:
            print('EL Producto carece de stock.')

    def json(self):
        import time
        dict={'Venta N°:':0,'Fecha:':time.strftime("%d/%m/%y"),'Cliente:':'carlos','lista de productos':self._Cesta_Venta,'subtotal:':'222','Total:':'33'}         
        p=[]
        r=[]
        [p.append(tuple((str(i),dict[i]))) for i in dict ]
        for i,e in p:
            if type(e) is list:
                for t in e:
                    r.append("Producto: {0} Precio: {1}".format(t['producto'],t['PV']))
            if type(e) is not list:
                r.append(str(str(i)+str(e)))
        return r

    def generar(self):
        self.__guargar_txt()

    def __guargar_txt(self):
        with open( ar+'\\Ventas','w') as archivo:
            archivo.write('*'*100+'\n')
            for i in self.json():
                archivo.write(i+'\n')
            archivo.write('*'*100+'\n')
        
    def verCesta(self):
        print('La cesta Actualmente contiene los siguientes Productos:')
        for i in self._Cesta_Venta:
                print(f"Producto:{i['producto']} PV:{i['PV']}")



