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

