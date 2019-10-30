import os

__nuevo= os.getcwd()
__nuevo.strip('\Modulo\config')

def Directorio():
        if 'base' not in os.listdir(__nuevo):      
                os.mkdir(__nuevo+'\\'+'base')
                directorio=__nuevo+'\\base'
                return directorio                
        else:
                return __nuevo+'\\base\\'

def crearArchivo(nombre):
        with open (str(Directorio())+'\\'+nombre,'a') as archivo:
                archivo.write('s')
        print('archivo creado bye')

