#from Productos import Producto
from config.archivos import Directorio,CargarDatos
from itertools import groupby
from time import time

class Compras:


    def __init__(self):
        #self.ObjProducto=Producto()
        self.__cestaCompra = []  # variable de clase.

    # Metodos de instancia.
    @property
    def getcesta(self):
        return CargarDatos(Compras.__name__)

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
        for i in range(0,int(registros)):

            self.ObjProducto.setNproducto = input(
                "Ingrese el nombre producto: ")
            self.ObjProducto.setCategoria = input(
                "Ingrese la Categoria del producto: ")
            self.ObjProducto.setCantidad = int(input(
                "cuantos Productos se han Comprado: "))

            if self.ObjProducto.Verficarproducto(self.ObjProducto.getNproduct) is False: #si no existe Agregar a base/Productos
                self.ObjProducto.agre_productos()
            else:# si existe el producto actualiar actualizar base/producto
                self.ObjProducto.actualizar_stock()

            precio = int(input('Ingrese el precio: '))
            diccionario = { '':self.ObjProducto,'Precio': str(precio)
                        }
            contenedor.append(diccionario)

        if len(contenedor) == int(registros):
            self.__guargar_txt(contenedor)
            print('Compra Reguistrada,Exitosamente.')

    def VerCompra(self):
        print("{:^10} {:^10} {:^10}".format(
            'Producto',  'Cantidad', 'PrecioCompra'))
        for i in self.getcesta:
            print(" {:^10} {:^10} {:^10} ".format(
                i['Producto'], i['Cantidad'], i['PrecioCompra']))

    def __guargar_txt(self, contenedor):
        import time
        with open(Directorio()+'Compras', 'a') as archivo:
            for i in contenedor:
                archivo.write("Producto:{0} Cantidad:{1} PrecioCompra:{2} Fecha_de_Registro_de_Compra:{3}\n".format(
                    i['Producto'], i['Cantidad'], i['Precio'],time.strftime("%d/%m/%y")))


    def Product_Fecha(self,res):
        if res ==1:
            r=input('Ingrese la fecha de compra en formato (dd/mm/aa) Ejemplo 12/11/19,\n Buscar: ')      
            dato='Fecha_de_Registro_de_Compra'
            mensaje='Productos Encontrados para la fecha: '
        elif res ==2:
            r=input('Ingrese el Nombre del producto a Buscar: ')      
            dato='Producto'
            mensaje='Producto: '    

        for key ,value in groupby(sorted (self.getcesta,key= lambda x: x[dato] ),lambda x:x[dato]  ):
            if r in key:
                print("Producto | Cantidad | PrecioCompra")
                for i in value:
                    print(f"{i['Producto']}         {i['Cantidad']}        ${i['PrecioCompra']}")
                return True
        print('No hay registros')

compra=Compras()
compra.VerCompra()