import os
import sys

def CrearDirectorio():
        if 'base' not in os.listdir(os.getcwd()):
                os.mkdir(os.getcwd()+'\\'+'base')
                directorio=os.getcwd()+'\\base'
                return directorio
        else:
                return os.getcwd()+'\\base'

def crearArchivo(nombre):
        directorio=CrearDirectorio()
        with open (directorio+'\\'+nombre,'a') as archivo:
                archivo.write('s')
        print('archivo creado bye')

