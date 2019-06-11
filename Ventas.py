from Compra import Compras

class VentaProductos(Compras):
    
    def __init__(self):
        self.PreciosProductos=[]
    
    def __buscarProducto(self,Nproduct):
        x=self.setc()
        for i in x:
            if Nproduct in i.values():
                return i,True
        return {},False


    def agre_productos(self,producto):
        i,r=self.__buscarProducto(producto)
        if  producto in i.values():
            pv=float(i['PrecioCompra'])*12/100
            self.PreciosProductos.append({'producto': producto,'PV':str(pv)})
            print('Producto agregado a la Cesta.')
        else:
            print('EL Producto carece de stock.')


    def verCesta(self):
        print('La cesta Actualmente contiene los siguientes Productos:')
        for i in self.PreciosProductos:
                print(f"Producto:{i['producto']} PV:{i['PV']}")
