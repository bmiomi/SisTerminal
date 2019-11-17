from .Personal import Personal

class PagosClientes ():
    
    def __init__(self):
            self.ObjPersonal=Personal()

    def Contado(self,valorCancelar):
        self.ObjPersonal.validar('Tatiana',123)
        print('valor de a cancelar:',valorCancelar)

    def Abonos(self,valorparcial):
        print('valor parcial a cancelar',valorparcial)
