class Personal:

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
    
    def _BuscarUsuario (self,nombre):
        for x in self.__Lusuarios:
            if   nombre == x['Usuario']:
                return x
        return None

    @property
    def getcargo(self):
        if self._BuscarUsuario(self.getUsuario) is not  None:
             return self._BuscarUsuario(self.getUsuario)['Cargo']

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
        if i is not None:
            self.SetUsuario=i['Usuario']
            self.SetPassword=str(i['contra'])

        if self.getUsuario is not  None and usuario==self.getUsuario  and self.getPassword is not None and contrasena==self.getPassword:
            self.Cargo=self.getcargo
            return True
        return False
