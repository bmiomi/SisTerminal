#from .Personas import Persona

class Empleados:

    __Lusuarios=[                
                {'Usuario':'Carlos','contra':134,'Cargo':'Cajero'},
                {'Usuario':'Mario','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Arturo','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Ernest','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Rodolfo','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Ricardo','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Maria','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Paola','contra':12,'Cargo':'ADMINISTRADOR'},
                {'Usuario':'Tatiana','contra':123,'Cargo':'ADMINISTRADOR'},
                {'Usuario':'marcelo','contra':123,'Cargo':'ADMINISTRADOR'}                
                ]

    def __init__(self):
        self.__nombreusuario=None
        self.__password=None
        self.__Cargo=None
  
    def __str__(self):
        return '{0},{1},{2}'.format(self.getUsuario,self.getPassword,self.getcargo() )

    @property
    def getUsuario(self):
        return self.__nombreusuario

    @getUsuario.setter
    def SetUsuario(self,nombre):
        self.__nombreusuario=nombre
    
    @property
    def getPassword(self):
        return self.__password

    @getPassword.setter
    def SetPassword(self,contra):
        self.__password= contra
    
    @property
    def getcargo(self):
        return self.__Cargo

    @getcargo.setter
    def SetCargo(self,cargo):
        self.__Cargo=cargo
    
    def _BuscarUsuario (self,nombre):
        print('valor a retornar al ejecutar esto :', nombre)
        for x in self.__Lusuarios:
            if x['Usuario'].find(nombre) != -1:
                return x

    def crearEmpleado(self,empleado,contrasena='default'):
        self.Lusuarios.append({'Usuario':empleado ,'contra':contrasena})

    def eliminarEmpleado(self,empleado):
        if empleado in self.Lusuarios:
            resp=input('Seguro desea Eliminar el cliente {0}: '.format(empleado))
            if resp in ('si','S','SI','s'):
                self.Lusuarios.remove(empleado)
                print ("Cliente: {0} Eliminado con exito ".format(empleado))
            else:
                print('El cliente {0} no se encuentra en este equipo'.format(empleado))
    
    def EditarEmpleados(self):
        pass
    
    def validar(self,usuario,contrasena):
        i=self._BuscarUsuario(usuario)
        if type(i) is dict:
            self.SetUsuario=i['Usuario']
            self.SetPassword=str(i['contra'])
            self.SetCargo=i['Cargo']
            return True
        return False
