import archivos
# esta clase debe tener un metodo que guarde los productos en un archivo txt.
class Productos():  

  def __init__(self,producto=None,Categoria=None):
    self.Nproducto=producto
    self.Categoria=Categoria
    self.__productos=list

  @property
  def getproducto(self):
        return self.__productos 

  @getproducto.setter
  def setproducto(self,producto):
        self.__productos=producto 
    
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
                    print('Producto Agregado')
                    return self.productos.append({'Producto':self.Nproducto,'Categoria': self.Categoria})
        else:
              print('El producto ya existe') 

# se insetan en el archivo txt la lista diccionario.
  
  def agregartxt(self):
    directorio=archivos.CrearDirectorio()
    with open( directorio+'\\'+'Productos','a') as productostxt:
      for i in self.productos:
        producto=i['Producto']
        Categoria=i['Categoria']
        productostxt.write(f'\nProducto:{producto} Categoria:{Categoria}')

  def eli_producto(self,producto):
    return self.productos.remove(producto)
  
  def actu_productos(self,nombreviejo,nuevonombre):
    return True

  def listarproductos(self):
    if len(self.__productos) == 0:
      self.cargarproductos()
    else:
      return self.__productos

# se visualiza por pantalla los productos Ingresados.
  def ver_todosproductos(self):
    self.cargarproductos()
    for i in self.__productos:
        print('=>',i) 

# se cargan los productos que se encuentran en archivo txt a la lista diccionario.
  def cargarproductos(self):
    del self.__productos[:]
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
          self.__productos.append(dic)
    return self.__productos
