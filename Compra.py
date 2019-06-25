from Productos import Productos
import archivos
directorio=archivos.CrearDirectorio()

class Compras(Productos):
    cestaCompra=[] #variable de instancia.
    
    @property
    def getcesta(self):
        return self.cestaCompra

    def VerficarCompra(self,nombre):
          directorio=archivos.CrearDirectorio()
          with open(directorio+'\\'+'Compras','r') as archivo:
              if nombre in archivo.read():
                return True
          return False

    def AgregaCompra(self):
        producto=input('Ingrese el Producto: ')
        b=self.Verficarproducto(producto)
        c=self.VerficarCompra(producto)
        if b is True:# verificamos que el producto exista en el archivo producto
            if c is not True:# verificamos que el producto este en el archivo compras
                cantidad=input('Ingrese la cantidad: ')
                PrecioCompra=input('Ingrese el Precio: ')
                self.__guargar_txt(producto,cantidad,PrecioCompra)
                print('Producto agregado,Exitosamente.')
            else:
                print('Existe una compra de ese producto')
        else:
            print('Producto inexistente,este debe ser Agregado Previamente')

    def VerCompra(self):
        self.__CargarCompras()
        print("{:^10} {:^10} {:^10}".format('Producto',  'Cantidad', 'PrecioCompra'))
        for i in self.cestaCompra:
            print(" {:^10} {:^10} {:^10} ".format(i['Producto'],i['Cantidad'],i['PrecioCompra']))

    def __guargar_txt(self,producto,cantidad,preciocompra):
        with open (directorio+'\\'+'Compras','a') as archivo:
            archivo.write(f'Producto:{producto} Cantidad:{str(cantidad)} PrecioCompra:{preciocompra}\n')

    def __CargarCompras(self):
        '''
        Se cargan los productos que se encuentran en archivo txt a la lista diccionario.
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
                  self.cestaCompra.append(dic)
        return self.getcesta
       
    def setc(self):
        return self.__CargarCompras()
