class Usuarios():

    Lusuarios=[                
                {'Usuario':'Carlos','contra':134,'Cargo':'Cajero'},
                {'Usuario':'Mario','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Arturo','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Ernest','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Rodolfo','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Ricardo','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Maria','contra':123,'Cargo':'Cajero'},
                {'Usuario':'Paola','contra':12,'Cargo':'ADMINISTRADOR'},
                {'Usuario':'Tatiana','contra':123,'Cargo':'ANALISTA'},
                {'Usuario':'marcelo','contra':123,'Cargo':'ANALISTA'}                
                ]

    def __init__(self,nombre,contra):
        self.nombreusuario=self.obtenerusuario(nombre)
        self.password=self.obtenerpassword(contra)
        self.Cargo=self.getcargo()
        self.Lusuarios
  
    def __str__(self):
        return '{0},{1},{2}'.format(self.nombreusuario,self.password,self.Cargo)

    def __BuscarUsuario (self,nombre):
        for x in self.Lusuarios:
            if  nombre == x['Usuario']:
                return x

    def obtenerusuario(self,nombre):
        if self.__BuscarUsuario(nombre) is not None and nombre in self.__BuscarUsuario(nombre)['Usuario']:
            return nombre

    def  obtenerpassword(self,contra):
        if self.__BuscarUsuario(self.getUsuario) is not None and contra == self.__BuscarUsuario(self.getUsuario)['contra']:
            return contra

    def getcargo(self):
        if self.__BuscarUsuario(self.getUsuario) is None:
            print('Cargo inexistente')
            return None
        else:
             return self.__BuscarUsuario(self.nombreusuario)['Cargo']

    @property
    def getUsuario(self):
        return self.nombreusuario

    @getUsuario.setter
    def SetUsuario(self,nombre):
        self.nombreusuario= self.obtenerusuario(nombre)
    
    @property
    def getPassword(self):
        return self.password

    @getPassword.setter
    def SetPassword(self,contra):
        self.password= self.obtenerpassword(contra)


    def crearEmpleado(self,empleado,contrasena='default'):
        self.Lusuarios.append({'Usuario':empleado ,'contra':contrasena})

    def eliminarEmpleado(self,empleado):
        if cliente in self.Lusuarios:
            resp=input('Seguro desea Eliminar el cliente {0}: '.format(empleado))
            if resp in ('si','S','SI','s'):
                self.Lusuarios.remove(empleado)
                print ("Cliente: {0} Eliminado con exito ".format(empleado))
            else:
                print('El cliente {0} no se encuentra en este equipo'.format(empleado))
    
    def EditarEmpleados(self):
        pass

    def validar(self,usuario,password):
       # print ( usuario,self.usuario,password,self.password)
        if usuario == self.usuario and password == self.password:
            self.getcargo()
            return True
        else:
            return False

