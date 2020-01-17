import os

__nuevo= os.getcwd().rstrip(' \Modulo')

def Directorio():
        if 'base' not in os.listdir(__nuevo):      
                os.mkdir(__nuevo+'\\'+'base')
                directorio=__nuevo+'\\base'
                return directorio                
        return __nuevo+'\\base\\'

def crearArchivo(nombre):
        with open (str(Directorio())+'\\'+nombre,'a') as archivo:
                archivo.write('s')
        print('archivo creado bye')

def CargarDatos(_file):
        __cestaCompra=[]
        with open ( Directorio()+ _file,'r') as File:
                p=[i.split() for i in File.readlines()]
                for x in range(len(p)):
                        __cestaCompra.append({key:value  for( key, value) in [ i.split(':') for i in p[x]] })
                return  __cestaCompra