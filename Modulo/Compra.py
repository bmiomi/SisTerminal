from .Productos import Productos
from .config.archivos import Directorio


class Compras:

    __cestaCompra = []  # variable de clase.

    def __init__(self):
        self.objtProducto = Productos()

    # Metodos de instancia.
    @property
    def getcesta(self):
        if len(self.__cestaCompra)==0:
            return self._CargarCompras()
        else:
            return self.__cestaCompra

     # ojo editar esta fucion "VerficarCompra" se debe registrar la compra
     # por lote y fecha

    def VerficarCompra(self, nombre):
          with open(Directorio()+'Compras', 'r') as archivo:
              if nombre in archivo.read():
                return True
          return False

    def AgregarCompra(self):
        contenedor = []
        diccionario = {}
        registros = int(input("Ingrese cuantos registros desea ingresar: "))
        for i in range(int(registros)):

            self.objtProducto.setNproducto = input(
                "Ingrese el nombre producto: ")
            self.objtProducto.setCategoria = input(
                "Ingrese la Categoria del producto: ")
            self.objtProducto.setCantidad = input(
                "cuantos Productos se han Comprado: ")

            if self.objtProducto.Verficarproducto(self.objtProducto.getNproduct) is False:
                self.objtProducto.agre_productos()
            else:
                self.objtProducto.actualizar_stock()

            precio = input('Ingrese el precio: ')
            diccionario = {'Producto': self.objtProducto.setNproducto, 'Categoria': self.objtProducto.setCategoria,
                         'Cantidad': self.objtProducto.setCantidad, 'Precio': precio
                        }
            contenedor.append(diccionario)

        if len(contenedor) == int(registros):
            self.__guargar_txt(contenedor)
            print('Compra Reguistrada,Exitosamente.')

    def VerCompra(self):
        self._CargarCompras()
        print("{:^10} {:^10} {:^10}".format(
            'Producto',  'Cantidad', 'PrecioCompra'))
        for i in self.__cestaCompra:
            print(" {:^10} {:^10} {:^10} ".format(
                i['Producto'], i['Cantidad'], i['PrecioCompra']))

    def __guargar_txt(self, contenedor):
        import time
        with open(Directorio()+'Compras', 'a') as archivo:
            for i in contenedor:
                archivo.write("Producto:{0} Cantidad:{1} PrecioCompra:{2} Fecha_de_Registro_de_Compra:{3}\n".format(
                    i['Producto'], i['Cantidad'], i['Precio'],time.strftime("%d/%m/%y-%H-%M-%S")))

    def _CargarCompras(self):
        '''
        Retorna una lista de diccionarios de archivo compras ubicado en el directorio base.
        '''
        with open(Directorio()+'Compras', 'r') as listadeclientes:
          contenedor = listadeclientes.read().split()
          lista1 = []
          lista2 = []
          dic={}
          for i in range(len(contenedor)):
              lista1.append(contenedor[i])
              if len(lista1) ==4:
                  lista2.append(lista1)  # N°Elementos
                  lista1 = []  # 0
          for i in lista2:
              for x in range(len(i)):
                  Compras.__cestaCompra.append(i[x].split(':'))
                  if len(Compras.__cestaCompra)==4:
                      lista1.append(Compras.__cestaCompra)
                      Compras.__cestaCompra=[]
          for i in lista1:
              Compras.__cestaCompra.append(dict(i))
          return Compras.__cestaCompra
    