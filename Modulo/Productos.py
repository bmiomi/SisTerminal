from config.archivos import Directorio,CargarDatos

class Producto:

      productos=[] # variable de clase
      
      def __init__(self,producto=None,Categoria=None,cantidad=None,unidad=None):
        self.Nproducto=producto
        self.Categoria=Categoria
        self.unidad=unidad
        self.cantidad=cantidad

      def __str__(self):
            return f'Producto:{self.Nproducto} Categoria:{self.Categoria} Cantidad:{self.cantidad} Unidad:{self.unidad}'

      @property
      def getproductos(self):
            return CargarDatos(Producto.__name__) 

      @property
      def getNproduct(self):
            return self.Nproducto

      @property
      def getCategoria(self):
            return self.Categoria

      @property
      def getCantidad(self):
            return self.cantidad

      @property
      def getUnidad(self):
            return self.unidad

# setter

      @getNproduct.setter
      def setNproducto(self,nombre):
            self.Nproducto=nombre

      @getCategoria.setter
      def setCategoria(self,categoria):
            self.Categoria=categoria

      @getCantidad.setter
      def setCantidad (self,cantidad):
            self.cantidad=cantidad

      @getUnidad.setter
      def setUnidad (self,unidad):
            self.unidad=unidad

      @staticmethod
      def Verficarproducto(nombre):
            with open(Directorio()+'\\'+'Productos','r') as archivo:
              if nombre in archivo.read():
                    return True  
            return False

#     se crean nuevos productos.
      def agre_productos(self):
            if self.Nproducto is not None and self.Categoria is not None and self.cantidad is not None:
                  self.__agregartxt()
                  return True

#     se Elimina los productos previa mente Ingresados.
      def eli_producto(self,producto):
        return self.productos.remove(producto)

      def actualizar_stock(self):
            for i in self.getproductos:
                  if self.getNproduct in i['Producto']:
                        i['Cantidad']=str(int(self.getCantidad)+int(i['Cantidad']))
                        with open(Directorio()+'\\'+'Productos','w') as productostxt:
                              for i in self.getproductos:
                                    productostxt.write(f"\nProducto:{i['Producto']} Categoria:{i['Categoria']} Cantidad:{i['Cantidad']}")

      def buscar_Producto(self,buscar):
            for  i  in  self.getproductos:
                  if buscar in i['Producto']:
                        return i
 
#     se visualiza por pantalla los productos Ingresados.
      def ver_todosproductos(self):
            for i in self.getproductos:
                  print(f"Producto:{i['Producto']} Categoria:{i['Categoria']} stock:{i['stock']} Unidad:{i['Unidad']}")

#     se insetan en el archivo txt la lista diccionario.    
      def __agregartxt(self):
        with open(Directorio()+'\\'+'Productos','a') as productostxt:
              productostxt.write(f'\nProducto:{self.Nproducto} Categoria:{self.Categoria} stock:{self.cantidad} Unidad:{self.unidad}')
