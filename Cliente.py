import config
import archivos
import random
directorio=archivos.CrearDirectorio()

class Cliente():

      def __init__(self):
            self.__clientes=[]            
      
      def __str__(self):
        return 'Cliente {0} Codigo: {1}'.format(self.nombre,self.codigo)
      
      @property
      def getcliente(self):
            self.__CargarClientes()
            return self.__clientes

      def agregarcliente(self,cliente):
            verficarcliente=self.__VerficarClienteArchivo(cliente)
            try:
              config.logging.debug('Proceso Agregar Cliente')
              if verficarcliente == False:
                self.__guargar_txt( cliente,codigo=random.randint(0,99999)) 
                print( "Cliente: {0} creado con exito ".format(cliente))
                config.logging.debug("Cliente: {0} creado con exito ".format(cliente))
              else:
                print( "Cliente: {0} no creado por que ya existe o su registro no fue el correcto.".format(cliente))
                config.logging.critical('Proceso no realizado,Cliente existente')
            finally:
                config.logging.info('Proceso  finalizado.')
    
      def modificarCliente(self):
            consulta = input('Escriba si o no en caso que desee modificar su Usuario :\n' '1)Si\n' '2)No ')
            if consulta  in ('Si','si','s','S'):
                  antiguo=input(' Dijite el nombre antiguo: ')
                  if self.__VerficarClienteArchivo(antiguo) is True:
                        with open( directorio+'\\'+'Clientes','r') as archivocliente:
                          archivoclienteread=archivocliente.read()
                          if antiguo in archivoclienteread:
                                with open( directorio+'\\'+'Clientes','w') as archivocliente1:
                                    Nuevo=input(' Dijite el Nuevo Nombre: ')
                                    archivocliente1.write(archivoclienteread.replace(antiguo,Nuevo))                      
                                print('El cambio de Usuario fue exitoso')
            else:              
              print('Entiendo,su modificasíon a sido cancelada')              

      def removercliente(self,cliente):
            with open (directorio+'\\'+'Clientes','r') as archivo:
                  archivoreadlines=archivo.readlines()
            for i in archivoreadlines:
                  if  cliente in i:
                    resp=input('Seguro desea Eliminar el cliente {0}: '.format(cliente))
                    if resp in ('si','S','SI','s'):
                          archivoreadlines.remove(i)
                          lista=[i.split() for i in archivoreadlines]
                          with open (directorio+'\\'+'Clientes','w') as archivo:
                                for i in range(len(lista)):
                                  archivo.write(lista[i][0]+' '+lista[i][1]+'\n')
                          print ("Cliente: {0} Eliminado con exito ".format(cliente))
                    else:
                            print('El cliente {0} no se encuentra en este equipo'.format(cliente))
      
      def buscarCliente(self,nombre):
            cargarclientes=self.__CargarClientes()
            for i in cargarclientes:
                  if nombre in i['Cliente']:
                        return f"Codigo:{i['Codigo']} Cliente:{i['Cliente']}"
            print("Cliente No Encontrado.")
            return False   

      def verclientes(self):
        print('N° Clientes: ',len(self.__CargarClientes()) )
        if len (self.__clientes)>=1:
            for i in self.__clientes:
              print(f"Cliente:{i['Cliente']} Codigo:{i['Codigo']}")
      
      def __VerficarClienteArchivo(self,nombre):
            '''Se verifica que el cliente exista en el archivo creado en caso de existir retornara un True'''
            with open(directorio+'\\'+'Clientes','r') as archivo:
              if nombre in archivo.read():
                    return True
              return False
  
      def __guargar_txt(self,cliente,codigo):
            with open (directorio+'\\'+'Clientes','a') as archivo:
              archivo.write(f'Cliente:{cliente} Codigo:{str(codigo)}\n')

      def __CargarClientes(self): 
      
        '''
          se cargan los productos que se encuentran en archivo txt a la lista diccionario.
        '''
        with open(directorio+'\\'+'Clientes','r') as listadeclientes:
          contenedor=listadeclientes.read().split()
          lista1=[elemento.split(':') for elemento in contenedor]
          dic={}
          for i,x in lista1:
                
                if 'Cliente' in i:
                      dic={i:x}
                if 'Codigo' in i:
                      dic[i]=x
                if len(dic)==2:
                      self.__clientes.append(dic)
          return self.__clientes
      
