import archivos
# esta clase debe tener un metodo que guarde los productos en un archivo txt.
class Productos():

      productos=[] # variable de clase
      def __init__(self,producto=None,Categoria=None):
        self.Nproducto=producto
        self.Categoria=Categoria

      @property
      def getproducto(self):
            if len(self.productos)==0:
                  return self.cargarproductos()
            else:
                  return self.productos 

      def Verficarproducto(self,nombre):
            directorio=archivos.CrearDirectorio()
            with open(directorio+'\\'+'Productos','r') as archivo:
              if nombre in archivo.read():
                    return True
            return False

      def agre_productos(self):
            verificarproducto=self.Verficarproducto(self.Nproducto)
            if verificarproducto is False:
                  if self.Nproducto is not None and self.Categoria is not None:
                        print(self.Nproducto,self.Categoria)
                        self.__agregartxt()
                        print('Producto Agregado')
            else:
                  print('El producto ya existe') 

      def eli_producto(self,producto):
        return self.productos.remove(producto)

      def actu_productos(self,nombreviejo,nuevonombre):
        return True

#     se visualiza por pantalla los productos Ingresados.
      def ver_todosproductos(self):
        self.cargarproductos()
        for i in self.productos:
            print('=>',i) 

#     se insetan en el archivo txt la lista diccionario.
      def __agregartxt(self):
        directorio=archivos.CrearDirectorio()
        with open( directorio+'\\'+'Productos','a') as productostxt:
              productostxt.write(f'\nProducto:{self.Nproducto} Categoria:{self.Categoria}')

#     se cargan los productos que se encuentran en archivo txt a la lista diccionario.
      def cargarproductos(self):
            directorio=archivos.CrearDirectorio()
            with open(directorio+'\\'+'Productos','r') as listadeproductos:
              contenedor=listadeproductos.read().split()
              lista1=[elemento.split(':') for elemento in contenedor]
              dic={}
              for i,x in lista1:
                if 'Producto' in i:
                  dic={i:x}
                if 'Categoria' in i:
                  dic[i]=x
                if len(dic)==2:
                  self.productos.append(dic)
            return self.getproducto