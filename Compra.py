from Productos import Productos
import archivos
directorio=archivos.CrearDirectorio()

class Compras(Productos):
    
    def __init__(self):
        self.__cestas=list
    
    @property
    def cesta(self):
        return self.__cestas

    @cesta.setter
    def cesta(self,cesta):
        '''
        cesta necesita un valor de tipo lista
        '''
        self.__cestas=cesta

    def __buscarProducto(self,Nproduct):
        self.cargarproductos()
        for i in self.productos:
            if Nproduct in i.values():
                return i,True
        return {},False
   
    def __guargar_txt(self,producto,cantidad,preciocompra):
        with open (directorio+'\\'+'Compras','a') as archivo:
            archivo.write(f'Producto:{producto} Cantidad:{str(cantidad)} PrecioCompra:{preciocompra}\n')

    def __CargarCompras(self):

        '''
        se cargan los productos que se encuentran en archivo txt a la lista diccionario.
        '''
        with open(directorio+'\\'+'Compras','r') as listadeclientes:
          contenedor=listadeclientes.read().split()
          lista1=[elemento.split(':') for elemento in contenedor]
          dic={}
          for i,x in lista1:
              if 'Producto' in i:
                  dic={i:x}
              if 'Cantidad' in i:
                  dic[i]=x
              if 'PrecioCompra' in i:
                   dic[i]=x
              if len(dic)==3:
                  self.__cestas.append(dic)
        return self.__cestas
       
    def setc(self):
        return self.__CargarCompras()

    def AgregaCompra(self):
        producto=input('Ingrese el Producto: ')
        i,b=self.__buscarProducto(producto)
        if b:
            if producto in i['Producto'] :
                cantidad=input('Ingrese la cantidad: ')
                PrecioCompra=input('Ingrese el Precio: ')
                self.__guargar_txt(producto,cantidad,PrecioCompra)
                print('Producto agregado,Exitosamente.')
        else:
            print('Producto inexistente,este debe ser Agregado Previamente')

    def VerCompra(self):
        self.__CargarCompras()
        for i in self.__cestas:
            print(i)

compra=Compras()
lista=['s','w']
print ('gett: ',compra.cesta)
print('setter: ',compra.cesta(lista))
