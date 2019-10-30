from .config.archivos import Directorio
# esta clase debe tener un metodo que guarde los productos en un archivo txt.

class Productos:

      productos=[] # variable de clase
      
      def __init__(self,producto=None,Categoria=None,cantidad=None):
        self.Nproducto=producto
        self.Categoria=Categoria
        self.cantidad=cantidad

      def __str__(self):
            return f'{self.Nproducto}'

      @property
      def getproductos(self):
            if len(self.productos)==0:
                  return self.cargarproductos()
            else:
                  return self.productos 

      @property
      def getNproduct(self):
            return self.Nproducto
      
      @property
      def getCategoria(self):
            return self.Categoria

      @property
      def getCantidad(self):
            return self.cantidad
# setter

      @getNproduct.setter
      def setNproducto(self,nombre):
            self.Nproducto=nombre.lower()

      @getCategoria.setter
      def setCategoria(self,categoria):
            self.Categoria=categoria.lower()

      @getCantidad.setter
      def setCantidad (self,cantidad):
            self.cantidad=cantidad

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
            else:
                  return False 

#     se Elimina los productos previa mente Ingresados.
      def eli_producto(self,producto):

        return self.productos.remove(producto)

#     se visualiza actualiza los productos previa mente Ingresados.
      def actu_productos(self):
            pass


      def actualizar_stock(self):
            for i in self.getproductos:
                  if self.getNproduct in i['Producto']:
                        i['Cantidad']=str(int(self.getCantidad)+int(i['Cantidad']))
                        self.setproductos=self.getproductos
                        with open(Directorio()+'\\'+'Productos','w') as productostxt:
                              for i in self.getproductos:
                                    productostxt.write(f"\nProducto:{i['Producto']} Categoria:{i['Categoria']} Cantidad:{i['Cantidad']}")

      def buscar_Producto(self,buscar):
            for  i  in  self.getproductos:
                  if buscar in i['Producto']:
                        return i
 
#     se visualiza por pantalla los productos Ingresados.
      def ver_todosproductos(self):
        self.cargarproductos()
        for i in self.productos:
            print('=>',i) 

#     se insetan en el archivo txt la lista diccionario.    
      def __agregartxt(self):
        with open(Directorio()+'\\'+'Productos','a') as productostxt:
              productostxt.write(f'\nProducto:{self.Nproducto} Categoria:{self.Categoria} Cantidad:{self.cantidad}')

#     se cargan los productos que se encuentran en archivo txt a la lista diccionario.

      def cargarproductos(self):
            with open(Directorio()+'\\'+'Productos','r') as listadeproductos:
              contenedor=listadeproductos.read().split()
              lista1=[]
              lista2=[]
              for i in  range(len(contenedor)):
                    lista1.append(contenedor[i])
                    if len(lista1) == 3:
                          lista2.append(lista1) # N°Elementos
                          lista1=[] # 0 
              for  i in lista2:
                    for x in range(len(i)):
                          self.productos.append(i[x].split(':'))
                          if len(self.productos)==3:
                                lista1.append(self.productos) # N° Elementos
                                self.productos=[] # 0
              for  i in lista1:
                    self.productos.append(dict(i))
              return self.productos

## funcion para ejecutar este modulo
def ModuloProdutos(Objproducto):
     try:
         while True:
                try:
                    respuesta=int(input('Seleccione una Opcion\t\n1) Crear producto\n2)Modificar Producto\n3)Eliminar Producto\n4)VerProductos\n5)regresar: '))
                    break
                except ValueError as e:
                    print(f'ADVERTENCIA : Valor ingresado Incorrecto se lanzo la excepcion de tipo: {e}')
       
         if respuesta == 1:
             prodc=int(input('Cuantos Productos Deseas Agregar: '))
             for i in range(prodc):
                 Objproducto.setNproducto=input('Dijiste el nombre del producto: ')
                 Objproducto.setCategoria=input('Dijiste la Categoria del producto: ') 
                 Objproducto.agre_productos()
         elif respuesta == 2:
             NombreViejo=input('Nombre del Producto que Deseas Modificar: ')
             nombreNuevo=input('Ingrese el Nuevo nombre: ')
             Objproducto.actu_productos(NombreViejo,nombreNuevo)
         elif respuesta ==3:
             pass
         elif respuesta ==4:
             Objproducto.ver_todosproductos()
           #  time.sleep(5)
         elif respuesta ==5:
            ModuloProdutos(Objproducto) # ojo revisar
     except KeyboardInterrupt:
         print('\n')
         print('*'*100)    
         print('Cerrando programa'.center(20))
         print('*'*100)

