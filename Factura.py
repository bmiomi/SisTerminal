class factura():
  
  __iva=12  
  def __init__(self,codigo,serie,numero):
      self.codigo=codigo
      self.serie=serie
      self.numero=numero
  
  def getnumero():
    if self.codigo is None:
      return 'no sea asignado un numero que identifique la factura'
    return 'numbero {}'.format(self.numero)

  def getserie():
    if self.serie is None:
      return 'no sea asignado una serie que identifique la factura'
    return 'serie {}'.format(self.serie)
  
  def getcodigo():
    if self.codigo is None:
      return 'no sea asignado un codigo que identifique la factura'
    return 'codigo {}'.format(self.codigo)  
  
  def getCabecera(self,cliente):
      print('''
      Factura : {0}   codigo: {1}  serie: {2} 
      +++++++++++++++++++++++++++++++++++++
      cliente: {3}'''.format(self.numero,self.codigo,self.serie,cliente))
      print('      +++++++++++++++++++++++++++++++++++++')
  
  def getdetalle(self,Cproduct):
    total=0
    for i in Cproduct:
      a=i['producto']
      b=i['Precio']
      c=i['Cantidad']
      print('''      cantidad   descripcion    precio 
          {0}       {1}         {2}'''.format(c,a,b))
      subtotal=c*b
      total+=subtotal
    print('      ................................')   
    print('      ...................total: {0}'.format(total))
                               